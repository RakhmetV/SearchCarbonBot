import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, name, college, date, case_number):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `users` (`user_id`, `name`, `date`, `college`, `case_number`, `status`) VALUES (?, ?, ?, ?, ?, ?)",
                (user_id, name, date, college, case_number, 0,))


    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def check_variant(self, date, case_number, variant):
        with self.connection:
            result = self.cursor.execute(
                "SELECT * FROM `users` WHERE `date` = ? and `case_number` = ? and `variant` = ?",
                (date, case_number, variant,)).fetchall()
            return bool(len(result))

    def get_variant(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                "SELECT `variant` FROM `users` WHERE `user_id` = ? ",
                (user_id,)).fetchall()
            return result

    def set_variant(self, user_id, variant):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `variant` = ? WHERE `user_id` = ?",
                                       (variant, user_id,))

    def set_answer_one(self, user_id, answer_one):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `answer_one` = ? WHERE `user_id` = ?",
                                       (answer_one, user_id,))

    def set_answer_two(self, user_id, answer_two):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `answer_two` = ? WHERE `user_id` = ?",
                                       (answer_two, user_id,))

    def set_status(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `status` = ? WHERE `user_id` = ?",
                                       (status, user_id,))

    def set_feedback(self, user_id, feedback):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `feedback` = ? WHERE `user_id` = ?",
                                       (feedback, user_id,))
