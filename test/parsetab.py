
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BKGDCOLOR CANVAS CIRCLE COLOR IMG LINE NUMBER OVAL RECT TEXT WRDexpression : CANVAS expression expressionexpression : BKGDCOLOR expression\n                  | BKGDCOLOR expression expression expressionexpression : NUMBERexpression : WRDexpression : COLOR expression\n                  | COLOR expression expression expressionexpression : LINE expression expression expression expressionexpression : CIRCLE expression expression expressionexpression : OVAL expression expression expression expressionexpression : RECT expression expression expression expressionexpression : TEXT expression expression expressionexpression : IMG expression expression expression expression'
    
_lr_action_items = {'CANVAS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[2,2,2,-4,-5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-1,2,2,2,2,2,2,2,2,-3,-7,2,-9,2,2,-12,2,-8,-10,-11,-13,]),'BKGDCOLOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[3,3,3,-4,-5,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-1,3,3,3,3,3,3,3,3,-3,-7,3,-9,3,3,-12,3,-8,-10,-11,-13,]),'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[4,4,4,-4,-5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-1,4,4,4,4,4,4,4,4,-3,-7,4,-9,4,4,-12,4,-8,-10,-11,-13,]),'WRD':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[5,5,5,-4,-5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-1,5,5,5,5,5,5,5,5,-3,-7,5,-9,5,5,-12,5,-8,-10,-11,-13,]),'COLOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[6,6,6,-4,-5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-1,6,6,6,6,6,6,6,6,-3,-7,6,-9,6,6,-12,6,-8,-10,-11,-13,]),'LINE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[7,7,7,-4,-5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-1,7,7,7,7,7,7,7,7,-3,-7,7,-9,7,7,-12,7,-8,-10,-11,-13,]),'CIRCLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[8,8,8,-4,-5,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-1,8,8,8,8,8,8,8,8,-3,-7,8,-9,8,8,-12,8,-8,-10,-11,-13,]),'OVAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[9,9,9,-4,-5,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-1,9,9,9,9,9,9,9,9,-3,-7,9,-9,9,9,-12,9,-8,-10,-11,-13,]),'RECT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[10,10,10,-4,-5,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-1,10,10,10,10,10,10,10,10,-3,-7,10,-9,10,10,-12,10,-8,-10,-11,-13,]),'TEXT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[11,11,11,-4,-5,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-1,11,11,11,11,11,11,11,11,-3,-7,11,-9,11,11,-12,11,-8,-10,-11,-13,]),'IMG':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,],[12,12,12,-4,-5,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-1,12,12,12,12,12,12,12,12,-3,-7,12,-9,12,12,-12,12,-8,-10,-11,-13,]),'$end':([1,4,5,14,15,22,31,32,34,37,39,40,41,42,],[0,-4,-5,-2,-6,-1,-3,-7,-9,-12,-8,-10,-11,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,33,35,36,38,],[1,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> CANVAS expression expression','expression',3,'p_expression_canvas','parser_dl.py',13),
  ('expression -> BKGDCOLOR expression','expression',2,'p_expression_bkgdcolor','parser_dl.py',17),
  ('expression -> BKGDCOLOR expression expression expression','expression',4,'p_expression_bkgdcolor','parser_dl.py',18),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser_dl.py',27),
  ('expression -> WRD','expression',1,'p_expression_word','parser_dl.py',31),
  ('expression -> COLOR expression','expression',2,'p_expression_color','parser_dl.py',36),
  ('expression -> COLOR expression expression expression','expression',4,'p_expression_color','parser_dl.py',37),
  ('expression -> LINE expression expression expression expression','expression',5,'p_expression_line','parser_dl.py',47),
  ('expression -> CIRCLE expression expression expression','expression',4,'p_expression_circle','parser_dl.py',56),
  ('expression -> OVAL expression expression expression expression','expression',5,'p_expression_oval','parser_dl.py',70),
  ('expression -> RECT expression expression expression expression','expression',5,'p_expression_rectangle','parser_dl.py',79),
  ('expression -> TEXT expression expression expression','expression',4,'p_expression_text','parser_dl.py',88),
  ('expression -> IMG expression expression expression expression','expression',5,'p_expression_image','parser_dl.py',98),
]