# Vision Agent (photo-only)

Дневное фото фасада → ночная концепция → правки. Без лендинга, без видео, без Max-бота.

## Запуск

1. Скопируйте `.env.example` → `.env`
2. Впишите `ROUTERAI_API_KEY=...`
3. Windows: `run_photo.bat`
4. Или: `python -m uvicorn cloud_app:app --host 127.0.0.1 --port 8080`
5. Откройте http://127.0.0.1:8080/studio

## Что внутри

- Vision Agent (фото)
- «Мои проекты» и история версий
- Референсы агента (`assets/agent_references`)

## Чего нет

- landing / сайт
- video / Seedance
- Max-бот
- реальные ключи (только пустой `.env.example`)
