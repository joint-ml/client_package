# Joint-ml
 
Данный пакет помогает реализовать удобный интрерфейс для использования вашей модели
в федеративном обучении на нашей платформе. 

## Содержание
- [Установка](#установка)
- [Создаем модуль](#шаг-1-создаем-модуль)
- [Импортируем Client](#шаг-2-импортируем)
- [Создаем класс и наследуем от Сlient](#шаг-3-создаем-класс-и-наследуем-от-client )
- [Реализуем необходимые методы ](#шаг-4-реализуем-необходимые-ьетоды)



## Установка 

Устанавливаем joint-ml с помощью pip:
```sh
pip install joint-ml
```

Или с помощью poetry:

```sh
poetry add joint-ml
```


## Создание клиента

### Требования
Для установки и запуска проекта, необходим Python>=!!.


### Шаг 1: Создаем модуль
Создайте python файл, который заканчивется "_client.py" в корневом каталоге вашего git репозитория. Например:
```sh
fl_client.py
```

### Шаг 2: Импортируем Client
Для создания интерфейса импортируе класс Client: 
```sh
from joint_ml import Client
```

### Шаг 3: Создаем класс и наследуем от Сlient 
Создаем класс, наследуемый от абстрактного класса Сlient
```sh
from joint_ml import Client


class FLClient(Client):
  ...
```

### Шаг 4: Реализуем необходимые методы 
Необходимо подготовить ваш код обучения модели для корректной работы на нашем сервисе. А именно, нужно реализовать 4 метода из класса Client:
```sh
from joint_ml import Client


class FLClient(Client):
    
  def get_weights():
    pass
    
  def set_weights():
    pass  
    
  def train():
    pass
    
  def test():
    pass
```

## Выкладываем код с реализованным классом Сlient в GitHub
Необходимо выложить готовый клиент в открытый GitHub репозиторий в ветку с именем master
