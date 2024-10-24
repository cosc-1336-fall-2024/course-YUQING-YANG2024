import unittest

#from tests.homework.b_in_proc_out import tests_in_proc_out

#from tests.homework.b_in_proc_out import tests_in_proc_out

#from tests.examples.b_input_process_output import tests_input_process_output

#from tests.homework.b_in_proc_out import tests_in_proc_out

#from tests.homework.c_decisions import tests_decisions #replace tests_in_proc_out with tests_decisions

#from tests.homework.d_repetition import tests_repetition

#from tests.homework.e_functions import tests_functions

from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
unittest.TextTestRunner(verbosity=2).run(suite)
