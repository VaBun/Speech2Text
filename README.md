Команда NO1

Цифровой Прорыв, финал, Кейс РБК.

Скачать модель vosk:
```
git clone https://github.com/alphacep/vosk-api
cd vosk-api/python/example
wget https://alphacephei.com/vosk/models/vosk-model-ru-0.22.zip
unzip vosk-model-ru-0.22.zip
mv vosk-model-ru-0.22.zip model
```
В файле app.py в Model("SOME_PATH"), заменить путь на путь до разархивированной модели.

Для запуска локального веб-интерфейса:
```
python app.py
```

Получение предсказаний модели через командную строку:
```
python asr_model.py videopath 'path' output 'file.txt'
```

Дмитрий Симаков, Василий Бунаков, Никита Чуркин, Евгений Хинензон.
