# Telegram Video Downloader ⚡

[![Stars](https://img.shields.io/github/stars/SEU_USERNAME/telegram-downloader?style=social)](https://github.com/SEU_USERNAME/telegram-downloader)
[![Forks](https://img.shields.io/github/forks/SEU_USERNAME/telegram-downloader)](https://github.com/SEU_USERNAME/telegram-downloader)
[![Issues](https://img.shields.io/github/issues/SEU_USERNAME/telegram-downloader)](https://github.com/SEU_USERNAME/telegram-downloader/issues)

**Baixe vídeos de canais Telegram 8x mais rápido** com downloads simultâneos e seleção inteligente via JSON.

## ✨ **Por que usar?**

| ⭐ **Recursos** | ✅ **Status** |
|---------------|-------------|
| 8 downloads simultâneos | ⚡ **Turbo** |
| Seleção via JSON | ✅ Simples |
| Auto-organização | 📁 Pastas nomeadas |
| 500+ vídeos por canal | 📚 Completo |
| Progresso visual | 👀 Real-time |

## 🚀 **Instalação (30s)**

```bash
git clone https://github.com/SEU_USERNAME/telegram-downloader.git
cd telegram-downloader
pip install -r requirements.txt
chmod +x tg_downloader.py
```

## ⚙️ **Configuração**

1. **Obtenha credenciais** (privado):
   ```
   my.telegram.org → API Development Tools
   Crie app → API_ID + API_HASH
   ```

2. **Edite** `tg_downloader.py`:
   ```python
   API_ID = 23726206           # Seu API_ID
   API_HASH = "c46f2a406..."  # Seu API_HASH  
   PHONE = "+551198673212"   # Seu número
   ```

⚠️ **NUNCA commite credenciais! Use `.env` ou variáveis**

## 🎮 **Uso**

```bash
python tg_downloader.py
```

```
⚡ /channels     → Lista seus canais
⚡ /list 123456  → Cria JSON de vídeos
⚡ /fast *.json  → Baixa 8 simultâneos!
```

### **Workflow completo:**
```
1. /channels
2. /list 2936789072    ← Copie ID
3. ls download/*.json  ← Veja JSON
4. nano download/*.json ← selected: true
5. /fast rapido_*.json
```

## 📁 **Estrutura gerada**
```
download/
├── rapido_123456789.json
└── FAST_BrSociety/
    ├── 12345_aula1.mp4  ← Nome + ID
    ├── 12346_aula2.mp4
    └── 12347_aula3.mp4
```

## ⚡ **Performance**
```
Velocidade: 8 downloads paralelos
Limite: 500 vídeos/scan
Chunk: Otimizado
Memória: < 100MB
```

## 🛠️ **Comandos**

| Comando | Descrição |
|---------|-----------|
| `/channels` | Lista todos canais |
| `/list ID` | Scan + JSON |
| `/fast arquivo.json` | Download turbo |
| `exit` | Sair |

## 📱 **Credenciais**
```
🔒 API_ID, API_HASH, PHONE = PRIVADO
❌ Nunca suba no GitHub!
✅ Use variáveis de ambiente
```

## 🤝 **Contribuições**
```
1. Fork projeto
2. Crie branch `feature/xyz`
3. Commit + PR
```

## 📄 **Licença**
MIT License - Use livremente!
