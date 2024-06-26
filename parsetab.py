
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPSMSleftTSDBMODrightPWSQASSIGN BREVE CHAR COMMENT DB EQ EQNOT GT GTOE HEXADECIMAL IAI ICLASSI IENUMI IFTHIS INI INTI IOI LBRACE LOOPFOR LPAREN LQUESTION LT LTOE MOD MS NEWCHAR NEWEXT NEWFUNC NEWINT NEWNUM NEWVAL NUMBER OTHERWISE PS PW RBRACE REAL RPAREN RQUESTION SEMICOLON SQ STRING TS WHILEFORprogram : statement_liststatement_list : statement\n                        | statement_list SEMICOLON statementstatement : assignment\n                    | expressionassignment : NEWVAL ASSIGN expressionexpression : expression PS term\n                    | expression MS term\n                    | termterm : term TS factor\n            | term DB factor\n            | term MOD factor\n            | factorfactor : NUMBER\n                | REAL\n                | LPAREN expression RPAREN'
    
_lr_action_items = {'NEWVAL':([0,12,],[6,6,]),'NUMBER':([0,11,12,13,14,15,16,17,18,],[9,9,9,9,9,9,9,9,9,]),'REAL':([0,11,12,13,14,15,16,17,18,],[10,10,10,10,10,10,10,10,10,]),'LPAREN':([0,11,12,13,14,15,16,17,18,],[11,11,11,11,11,11,11,11,11,]),'$end':([1,2,3,4,5,7,8,9,10,20,21,22,23,24,25,26,27,],[0,-1,-2,-4,-5,-9,-13,-14,-15,-3,-7,-8,-6,-10,-11,-12,-16,]),'SEMICOLON':([2,3,4,5,7,8,9,10,20,21,22,23,24,25,26,27,],[12,-2,-4,-5,-9,-13,-14,-15,-3,-7,-8,-6,-10,-11,-12,-16,]),'PS':([5,7,8,9,10,19,21,22,23,24,25,26,27,],[13,-9,-13,-14,-15,13,-7,-8,13,-10,-11,-12,-16,]),'MS':([5,7,8,9,10,19,21,22,23,24,25,26,27,],[14,-9,-13,-14,-15,14,-7,-8,14,-10,-11,-12,-16,]),'ASSIGN':([6,],[15,]),'RPAREN':([7,8,9,10,19,21,22,24,25,26,27,],[-9,-13,-14,-15,27,-7,-8,-10,-11,-12,-16,]),'TS':([7,8,9,10,21,22,24,25,26,27,],[16,-13,-14,-15,16,16,-10,-11,-12,-16,]),'DB':([7,8,9,10,21,22,24,25,26,27,],[17,-13,-14,-15,17,17,-10,-11,-12,-16,]),'MOD':([7,8,9,10,21,22,24,25,26,27,],[18,-13,-14,-15,18,18,-10,-11,-12,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,12,],[3,20,]),'assignment':([0,12,],[4,4,]),'expression':([0,11,12,15,],[5,19,5,23,]),'term':([0,11,12,13,14,15,],[7,7,7,21,22,7,]),'factor':([0,11,12,13,14,15,16,17,18,],[8,8,8,8,8,8,24,25,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','my_parser.py',14),
  ('statement_list -> statement','statement_list',1,'p_statement_list','my_parser.py',18),
  ('statement_list -> statement_list SEMICOLON statement','statement_list',3,'p_statement_list','my_parser.py',19),
  ('statement -> assignment','statement',1,'p_statement','my_parser.py',26),
  ('statement -> expression','statement',1,'p_statement','my_parser.py',27),
  ('assignment -> NEWVAL ASSIGN expression','assignment',3,'p_assignment','my_parser.py',31),
  ('expression -> expression PS term','expression',3,'p_expression','my_parser.py',35),
  ('expression -> expression MS term','expression',3,'p_expression','my_parser.py',36),
  ('expression -> term','expression',1,'p_expression','my_parser.py',37),
  ('term -> term TS factor','term',3,'p_term','my_parser.py',47),
  ('term -> term DB factor','term',3,'p_term','my_parser.py',48),
  ('term -> term MOD factor','term',3,'p_term','my_parser.py',49),
  ('term -> factor','term',1,'p_term','my_parser.py',50),
  ('factor -> NUMBER','factor',1,'p_factor','my_parser.py',62),
  ('factor -> REAL','factor',1,'p_factor','my_parser.py',63),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','my_parser.py',64),
]
