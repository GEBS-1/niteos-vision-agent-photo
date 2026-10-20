# Vision Agent (photo-only)

Дневное фото фасада → ночная концепция → правки в чате.

Видео (Seedance/ffmpeg), Max-бот и авторизация Max полностью удалены.

## Запуск

1. Скопируйте `.env.example` → `.env` и вставьте `ROUTERAI_API_KEY`
2. `run_photo.bat` или `python -m uvicorn cloud_app:app --host 127.0.0.1 --port 8080`
3. Откройте http://127.0.0.1:8080/studio

## Состав

- Vision Agent (фото)
- «Мои проекты» (локальные проекты на диске)
- Референсы `assets/agent_references`
