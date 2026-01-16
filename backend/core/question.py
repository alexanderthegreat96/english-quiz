from typing import Optional

class Question:
    def __init__(self, data: Optional[list[dict]], provided_answers: list[str]) -> None:
        self.questions: list[dict] = data if data is not None else []
        self.provided_answers: list[str] = provided_answers
        
    def __check_integrity(self) -> bool:
        if not self.questions:
            return False
        
        required_keys = ["question", "answer", "variants", "is_correct"]
        for item in self.questions:
            if not all(key in item for key in required_keys):
                return False
        return True
    
    def get_rendered_question(self, index: int, show_answer: bool = False) -> str:
        """Replaces the {blank} placeholder with either the correct word or underscores."""
        question_dict = self.questions[index]
        placeholder = "__________"
        
        if show_answer:
            correct_idx = question_dict["answer"]
            placeholder = question_dict["variants"][correct_idx]
            
        return question_dict["question"].replace("{blank}", placeholder)
    
    def validate(self) -> list[dict]:
        if not self.__check_integrity():
            raise ValueError('Invalid data structure.')

        if not self.provided_answers:
            raise ValueError('No answers were provided.')

        for i in range(len(self.provided_answers)):
            if i >= len(self.questions):
                break 
            
            user_str = self.provided_answers[i]
            current_q = self.questions[i]
            
            correct_index = current_q["answer"]
            correct_word = current_q["variants"][correct_index]
            
            if user_str.strip().lower() == correct_word.strip().lower():
                current_q["is_correct"] = True
            else:
                current_q["is_correct"] = False
        
        return self.questions