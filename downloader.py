#!/usr/bin/env python3
import json
import asyncio
from pathlib import Path
from telethon import TelegramClient
from telethon.tl.types import DocumentAttributeFilename

API_ID = 999999
API_HASH = "999999999999999999999999999999"
PHONE = "+5511999999999"
SAVE_PATH = Path("download")
SAVE_PATH.mkdir(parents=True, exist_ok=True)

client = None
semaphore = asyncio.Semaphore(8)


def clean_filename(name):
    return name.replace("/", "_").replace("\\", "_").replace(":", "_")[:80]


def is_video(doc):
    return doc.mime_type.startswith("video/")


async def safe_download(msg, path):
    async with semaphore:
        print(f"⬇️ {path.name}...", end=" ")
        await client.download_media(msg, file=path)
        print("✅")


async def list_videos(channel_id):
    entity = await client.get_entity(channel_id)
    print(f"\n📥 '{entity.title}'...")
    videos = []

    async for msg in client.iter_messages(entity, reverse=True, limit=500):
        if msg.document and is_video(msg.document):
            filename = "video.mp4"
            for attr in msg.document.attributes:
                if hasattr(attr, "file_name"):
                    filename = attr.file_name
                    break
            videos.append(
                {
                    "msg_id": msg.id,
                    "filename": f"{msg.id}_{clean_filename(filename)}",
                    "size_mb": f"{msg.document.size/1024/1024:.0f}MB",
                    "selected": True,
                }
            )

    if videos:
        json_name = f"fast_{abs(entity.id)}.json"
        (SAVE_PATH / json_name).write_text(
            json.dumps(videos, indent=2, ensure_ascii=False)
        )
        print(f"✅ {len(videos)} videos → {SAVE_PATH / json_name}")
        return json_name
    print("❌ No videos")


async def fast_download(json_filename):
    videos = json.loads((SAVE_PATH / json_filename).read_text())
    selected = [v for v in videos if v["selected"]]
    if not selected:
        print("❌ No selected videos!")
        return

    channel_id = int(json_filename.split("_")[-1].replace(".json", ""))
    entity = await client.get_entity(channel_id)
    folder = SAVE_PATH / f"FAST_{entity.title[:40]}"
    folder.mkdir(exist_ok=True)

    tasks = []
    print(f"⚡ Starting {len(selected)} parallel downloads...")

    for video in selected:

        async def download_one(msg_id=video["msg_id"], filename=video["filename"]):
            async for msg in client.iter_messages(entity, limit=1000):
                if msg.id == msg_id and msg.document:
                    await safe_download(msg, folder / filename)
                    break

        tasks.append(download_one())
        if len(tasks) >= 8:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []

    if tasks:
        await asyncio.gather(*tasks)


async def list_channels():
    print("📺 Channels:")
    count = 0
    async for dialog in client.iter_dialogs(limit=50):
        if dialog.is_channel:
            print(f"  {dialog.name} → /list {dialog.entity.id}")
            count += 1
    print(f"Total: {count}")


async def main():
    global client
    client = TelegramClient("session_user", API_ID, API_HASH)
    await client.start(phone=PHONE)
    print("⚡ FAST MODE! (8 parallel downloads)")
    print("💬 /list ID | /fast filename.json | /channels")

    while True:
        cmd = input("⚡ ").strip()
        if not cmd:
            continue

        if cmd == "exit":
            break
        elif cmd.startswith("/channels"):
            await list_channels()
        elif cmd.startswith("/list"):
            channel_id = cmd.split()[1] if len(cmd.split()) > 1 else ""
            if channel_id:
                await list_videos(channel_id)
        elif cmd.startswith("/fast"):
            filename = cmd.split()[1] if len(cmd.split()) > 1 else ""
            if filename:
                await fast_download(filename)
        else:
            print("❓ /list ID | /fast filename.json | /channels")


if __name__ == "__main__":
    asyncio.run(main())
