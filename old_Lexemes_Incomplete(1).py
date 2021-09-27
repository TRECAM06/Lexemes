from typing import Dict, List, Tuple

### ======================================== Tokens ======================================== ###

class _Token_Enum():
    def __init__(self) -> None:
        class _Operators():
            def __init__(self) -> None:
                self.Add = "+"
                self.Subtract = "-"
                self.Multiply = "*"
                self.Division = "/"
                self.Power = "**"
                self.Int_Division = "//"
                self.Modulo = "%"
                self.Bitwise_And = "&"
                self.Bitwise_Or = "|"
                self.Bitwise_Xor  = "^"
                self.Bitwise_Not  = "~"
                self.Bitshift_Right = ">>"
                self.Bitshift_Left = "<<"
                self.And = "&&"
                self.Or = "||"
                self.Not_Equal = "!="
                self.Double_Equal = "=="
                self.Not = "!"
                self.Less = "<"
                self.Less_Equal = "<="
                self.Greater = ">"
                self.Greater_Equal = ">="
                self.Equal = "="
            def __repr__(self) -> str:
                return str(vars(self))
        self.Operators = _Operators()

        class _Closures():
            def __init__(self) -> None:
                self.Paren_Open = "("
                self.Paren_Close = ")"
                self.Square_Open = "["
                self.Square_Close = "]"
                self.Curly_Open = "{"
                self.Curly_Close = "}"
            def __repr__(self) -> str:
                return str(vars(self))
        self.Closures = _Closures()

        class _Keywords():
            def __init__(self) -> None:
                self.If = "if"
                self.Else = "else"
                self.While = "while"
            def __repr__(self) -> str:
                return str(vars(self))
        self.Keywords = _Keywords()

        class _Functions():
            def __init__(self) -> None:
                self.Log = "log"
                self.Print = "print"
                self.To_Int = "to_int"
                self.To_Float = "to_float"
                self.To_Bool = "to_bool"
                self.To_String = "to_string"
            def __repr__(self) -> str:
                return str(vars(self))
        self.Functions = _Functions()

        class _Literals():
            def __init__(self) -> None:
                self.Int = "int"
                self.Float = "float"
                self.Bool = "bool"
                self.String = '"*"'
            def __repr__(self) -> str:
                return str(vars(self))
        self.Literals = _Literals()
        
        class _Comments():
            def __init__(self) -> None:
                self.Comment = "#"
                self.Block_Comment_Open = '/*'
                self.Block_Comment_Close = '*/'
            def __repr__(self) -> str:
                return str(vars(self))
        self.Comments = _Comments()

        class _Line_End():
            def __init__(self) -> None:
                self.Line_End = ";"
            def __repr__(self) -> str:
                return str(vars(self))
        self.Line_End = _Line_End()

    def __repr__(self) -> str:
        return str(vars(self))
Token_Enum = _Token_Enum()



### ======================================== Lexemes ======================================== ###

class _Lexeme_State_Enum():
    def __init__(self) -> None:
        self.failed = "failed"
        self.open = "open"
        self.complete = "complete"

    def __repr__(self) -> str:
        return str(vars(self))
Lexeme_State_Enum = _Lexeme_State_Enum()


class Lexeme():

    def __init__(self) -> None:
        self.reset()
        self._token = None

    ### Setters
    def reset(self) -> None:
        self._captured = []
        self._state = Lexeme_State_Enum.open
        self._mode = 0

    def set_fail(self) -> None:
        self._state = Lexeme_State_Enum.failed

    def set_complete(self) -> None:
        self._state = Lexeme_State_Enum.complete
    
    ### Getters
    def feed(self, char: str, remaining: List[str]) -> int:
        print("AEC")
        return self._state

    def is_open(self) -> bool:
        return self._state == Lexeme_State_Enum.open

    def is_failed(self) -> bool:
        return self._state == Lexeme_State_Enum.failed

    def is_complete(self) -> bool:
        return self._state == Lexeme_State_Enum.complete

    def get_state(self) -> int:
        return self._state

    def get_captured(self) -> str:
        return "".join(self._captured)

    def get_token(self) -> str:
        return self._token


class Lexeme_Single_Char(Lexeme):

    def __init__(self, char, token) -> None:
        super().__init__()
        self._token = token
        self._char = char
    
    def feed(self, char: str, remaining: List[str]) -> int:
        if not self.is_open():
            return self._state

        if char == self._char:
            pass
        else:
            pass

        return self._state


class Lexeme_Double_Char(Lexeme):

    def __init__(self, char_1, char_2, token) -> None:
        super().__init__()
        self._token = token
        self._char_1 = char_1
        self._char_2 = char_2
    
    def feed(self, char: str, remaining: List[str]) -> int:
        if not self.is_open():
            return self._state

        if self._mode == 0:
            pass
        else:
            pass

        return self._state


class Lexeme_Multi_Char(Lexeme):
    pass

### ======================================== Lexemes / Operators - Double ======================================== ###


# self.Power = "**"
class Lxm_Op_Power(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('*', '*', Token_Enum.Operators.Power)


# self.Int_Division = "//"
class Lxm_Op_Int_Division(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('/', '/', Token_Enum.Operators.Int_Division)


# self.Bitshift_Right = ">>"
class Lxm_Op_Bitshift_Right(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('>', '>', Token_Enum.Operators.Bitshift_Right)


# self.Bitshift_Left = "<<"
class Lxm_Op_Bitshift_Left(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('<', '<', Token_Enum.Operators.Bitshift_Left)


# self.And = "&&"
class Lxm_Op_And(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('&', '&', Token_Enum.Operators.And)


# self.Or = "||"
class Lxm_Op_Or(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('|', '|', Token_Enum.Operators.Or)


# self.Not_Equal = "!="
class Lxm_Op_Not_Equal(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('!', '=', Token_Enum.Operators.Not_Equal)


# self.Double_Equal = "=="
class Lxm_Op_Double_Equal(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('=', '=', Token_Enum.Operators.Double_Equal)


# self.Less_Equal = "<="
class Lxm_Op_Less_Equal(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('<', '=', Token_Enum.Operators.Less_Equal)


# self.Greater_Equal = ">="
class Lxm_Op_Greater_Equal(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('>', '=', Token_Enum.Operators.Greater_Equal)


### ======================================== Lexemes / Operators - Single ======================================== ###


# self.Add = "+"
class Lxm_Op_Add(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('+', Token_Enum.Operators.Add)


# self.Subtract = "-"
class Lxm_Op_Subtract(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('-', Token_Enum.Operators.Subtract)


# self.Multiply = "*"
class Lxm_Op_Multiply(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('*', Token_Enum.Operators.Multiply)


# self.Division = "/"
class Lxm_Op_Division(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('/', Token_Enum.Operators.Division)


# self.Modulo = "%"
class Lxm_Op_Modulo(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('%', Token_Enum.Operators.Modulo)


# self.Bitwise_And = "&"
class Lxm_Op_Bitwise_And(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('&', Token_Enum.Operators.Bitwise_And)


# self.Bitwise_Or = "|"
class Lxm_Op_Bitwise_Or(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('|', Token_Enum.Operators.Bitwise_Or)


# self.Bitwise_Xor  = "^"
class Lxm_Op_Bitwise_Xor(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('^', Token_Enum.Operators.Bitwise_Xor)


# self.Bitwise_Not  = "~"
class Lxm_Op_Bitwise_Not(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('~', Token_Enum.Operators.Bitwise_Not)


# self.Not = "!"
class Lxm_Op_Not(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('!', Token_Enum.Operators.Not)


# self.Less = "<"
class Lxm_Op_Less(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('<', Token_Enum.Operators.Less)


# self.Greater = ">"
class Lxm_Op_Greater(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('>', Token_Enum.Operators.Greater)


# self.Equal = "="
class Lxm_Op_Equal(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('=', Token_Enum.Operators.Equal)


### ======================================== Lexemes / Closures ======================================== ###


# self.Paren_Open = "("
class Lxm_Close_Paren_Open(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('(', Token_Enum.Closures.Paren_Open)


# self.Paren_Close = ")"
class Lxm_Close_Paren_Close(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__(')', Token_Enum.Closures.Paren_Close)

        
# self.Square_Open = "["
class Lxm_Close_Square_Open(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('[', Token_Enum.Closures.Square_Open)

        
# self.Square_Close = "]"
class Lxm_Close_Square_Close(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__(']', Token_Enum.Closures.Square_Close)

        
# self.Curly_Open = "{"
class Lxm_Close_Curly_Open(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('{', Token_Enum.Closures.Curly_Open)

        
# self.Curly_Close = "}"
class Lxm_Close_Curly_Close(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('}', Token_Enum.Closures.Curly_Close)

        
### ======================================== Lexemes / Keywords ======================================== ###


# self.If = "if"
# self.Else = "else"
# self.While = "while"


### ======================================== Lexemes / Functions ======================================== ###


# self.Log = "log"
# self.Print = "print"
# self.To_Int = "to_int"
# self.To_Float = "to_float"
# self.To_Bool = "to_bool"
# self.To_String = "to_string"


### ======================================== Lexemes / Literals ======================================== ###


# self.Int = "int"
# self.Float = "float"
# self.Bool = "bool"
# self.String = '"*"'


### ======================================== Lexemes / Comments ======================================== ###


# self.Comment = "#"
class Lxm_Close_Comment(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__('#', Token_Enum.Comments.Comment)


# self.Block_Comment_Open = '/*'
class Lxm_Comments_Block_Comment_Open(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('/', '*', Token_Enum.Comments.Block_Comment_Open)


# self.Block_Comment_Close = '*/'
class Lxm_Comments_Block_Comment_Close(Lexeme_Double_Char):

    def __init__(self) -> None:
        super().__init__('*', '/', Token_Enum.Comments.Block_Comment_Close)


### ======================================== Lexemes / Line_End ======================================== ###


# self.Line_End = ";"
class Lxm_Line_End(Lexeme_Single_Char):

    def __init__(self) -> None:
        super().__init__(';', Token_Enum.Line_End.Line_End)

