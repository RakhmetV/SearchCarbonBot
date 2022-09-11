import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, name, date):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `users` (`user_id`, `name`, `date`, `status`) VALUES (?, ?, ?, ?)",
                (user_id, name, date, 0,))

    # поиск пользователя по его ID
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    # подсчет количества вариантов в одном кейсе
    def counting_variant_case(self, case_number, date):
        with self.connection:
            result = self.cursor.execute(
                "SELECT COUNT(`variant`) FROM `users` WHERE `date` = ? and `case_number` = ? and `status` = ?",
                (date, case_number, 0,)).fetchall()
            return result

    # Проверка на наличие варианта
    def check_variant(self, date, case_number, variant):
        with self.connection:
            result = self.cursor.execute(
                "SELECT * FROM `users` WHERE `date` = ? and `case_number` = ? and `status` = ? and `variant` = ? ",
                (date, case_number, 0, variant,)).fetchall()
            return bool(len(result))

    # Поиск варианта у пользователя
    def get_variant(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                "SELECT `variant` FROM `users` WHERE `user_id` = ? ",
                (user_id,)).fetchall()
            return result

    def set_district(self, user_id, variant):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `variant` = ? WHERE `user_id` = ?",
                                       (variant, user_id,))

    def set_college(self, user_id, college):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `college` = ? WHERE `user_id` = ?",
                                       (college, user_id,))

    def set_case_number(self, user_id, case_number):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `case_number` = ? WHERE `user_id` = ?",
                                       (case_number, user_id,))

    def set_district(self, user_id, district):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `district` = ? WHERE `user_id` = ?",
                                       (district, user_id,))

    def set_password(self, user_id, password):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `password` = ? WHERE `user_id` = ?",
                                       (password, user_id,))

    def set_variant(self, user_id, district):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `district` = ? WHERE `user_id` = ?",
                                       (district, user_id,))

    # добавить ответ на вопрос 1
    def set_answer_one(self, user_id, answer_one):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `answer_one` = ? WHERE `user_id` = ?",
                                       (answer_one, user_id,))

    # добавить ответ на вопрос 2
    def set_answer_two(self, user_id, answer_two):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `answer_two` = ? WHERE `user_id` = ?",
                                       (answer_two, user_id,))

    # уставнока статуса
    def set_status(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `user_id` = ?",
                                       (status, user_id,))

    # установка отзыва
    def set_feedback(self, user_id, feedback):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `feedback` = ? WHERE `user_id` = ?",
                                       (feedback, user_id,))

    def del_user(self, user_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM `users` WHERE user_id = ?", (user_id,))

    def del_all_users(self):
        with self.connection:
            return self.cursor.execute("DELETE FROM `users`")

    # данные о пользователях за сегодня
    def get_user_today(self, date):
        with self.connection:
            return self.cursor.execute(
                "SELECT `name`, `college`, `date`, `variant`, `answer_one`, `answer_two`, `feedback` FROM `users` WHERE date = ?",
                (date,)).fetchall()

    def get_user_all(self):
        with self.connection:
            return self.cursor.execute(
                "SELECT `name`, `college`, `date`, `variant`, `answer_one`, `answer_two`, `feedback` FROM `users`").fetchall()
