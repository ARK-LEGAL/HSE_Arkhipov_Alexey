class CourtCase:
    def init(self, case_number: str):
        self.case_number = case_number
        self.case_participants = []
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ""

    def set_a_listening_datetime(self, datetime: str, description: str = ""):
        """Добавляет дату и время судебного заседания."""
        self.listening_datetimes.append({
            "datetime": datetime,
            "description": description
        })

    def add_participant(self, participant_inn: str):
        """Добавляет участника по ИНН."""
        if participant_inn not in self.case_participants:
            self.case_participants.append(participant_inn)

    def remove_participant(self, participant_inn: str):
        """Убирает участника по ИНН."""
        if participant_inn in self.case_participants:
            self.case_participants.remove(participant_inn)

    def make_a_decision(self, verdict: str):
        """Выносит решение по делу."""
        self.verdict = verdict
        self.is_finished = True
