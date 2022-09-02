import sqlite3


class Database:
    def __int__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, name, college, date, case_number):
        with self.connection:
            self.cursor.execute("INSERT INTO `users` (`user_id`, `name`, `date`, `college`, `case_number`) "
                                "VALUE (?)", (user_id, name, date, college, case_number,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_answer_one(self, user_id, answer_one):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `answer_one` = ? WHERE `user_id` = ?",
                                       (answer_one, user_id,))

    def set_answer_two(self, user_id, answer_two):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `answer_two` = ? WHERE `user_id` = ?",
                                       (answer_two, user_id,))

    def set_feedback(self, user_id, feedback):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `feedback` = ? WHERE `user_id` = ?",
                                       (feedback, user_id,))
