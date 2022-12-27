class Expressions:

    # before using the function we need to separate the expression from the full sentence! --
    #                                                                                       |
    # (will have a static function that does that on this class)               <-------------
    # Ex: "I am not happy with this action" => to => "not happy"
    @staticmethod
    def check_if_switched_meaning(expression: str):
        if expression.split()[0] == "not":
            return True
        return False

    # before using the function we need to separate the expression from the full sentence! --
    #                                                                                       |
    # (will have a static function that does that on this class)               <-------------
    # Ex: "I am not happy with this action" => to => "not happy"
    def check_expression_type(self, expression: str, expression_list: list, initial_expression_type: str):
        expression_type = ""
        if any(exp in expression for exp in expression_list):
            if initial_expression_type == "good":
                if self.check_if_switched_meaning(expression):
                    expression_type = "bad"
                else:
                    expression_type = "good"
            else:
                if self.check_if_switched_meaning(expression):
                    expression_type = "good"
                else:
                    expression_type = "bad"
            return expression_type
        else:
            raise ValueError("expression not in expression list!")  # TODO: change to custom error.
