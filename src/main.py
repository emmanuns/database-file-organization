from FixedHeap import FixedSizeHeap
from VariableHeap import VariableSizeHeap

fixed_heap = FixedSizeHeap(record_size=256, filename='fixed_records.json')
variable_heap = VariableSizeHeap(filename='variable_records.json')


#fixed_heap.insert({"key": "123", "value": "Registro 1"})
#variable_heap.insert({"key": "abc", "value": "Registro A"})
