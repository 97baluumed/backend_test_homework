class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.trainig_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Выводит результат тренировки"""
        message = (
            f'Тип тренировки: {self.trainig_type};'
            f'Длительность: {self.duration:.3f} ч.;'
            f'Дистанция: { self.distance:.3f} км;'
            f'Средняя скорость: {self.speed:.3f} км/ч;'
            f'Потрачено ккал: {self.calories:.3f}.'
                  )
        return message


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    MIN_IN_H = 60
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight    
        
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_info = InfoMessage(self.__class__.__name__,
                                    self.training_type,
                                    self.duration,
                                    self.get_distance(),
                                    self.get_mean_speed(),
                                    self.get_spent_calories()
                                    )
        return training_info

class Running(Training):
    """Тренировка: бег."""
    M_IN_KM = 1000
    MIN_IN_H = 60
    LEN_STEP = 0.65  

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        spent_calories = (18 * self.get_mean_speed - 20) * self.weight / self.M_IN_KM * self.duration
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    M_IN_KM = 1000
    MIN_IN_H = 60
    LEN_STEP = 0.65  

    def __init__(self, action, duration, weight, height) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        spent_calories = (0.035 * self.weight + (self.get_mean_speed**2 // self.height) * 0.029 * self.weight) * self.duration
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    M_IN_KM = 1000
    MIN_IN_H = 60
    LEN_STEP = 1.38

    def __init__(self, action, duration, weight, length_pool, count_pool) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.length_pool * self.count_pool / self.M_IN_KM / (self.duration / self.MIN_IN_H)
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        spent_calories = (self.mean_speed + 1.1) * 2 * self.self.weight
        return spent_calories


def read_package(workout_type: str,
                 data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_t = {"SWM": Swimming,
                  "RUN": Running,
                  "WLK": SportsWalking}
    action, duration, weight, *other = data
    if workout_type == 'SWM' and workout_type == training_t.keys():
        lenght_pool, swiming_loop = other
        return Swimming(action, duration, weight, lenght_pool, swiming_loop)
    elif workout_type == 'RUN' and workout_type == training_t.keys():
        return Running(action, duration, weight)
    elif workout_type == 'WLK' and workout_type == training_t.keys():
        height = other[0]
        return SportsWalking(action, duration, weight, height)


def main(training: Training):
    """Главная функция."""

    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

