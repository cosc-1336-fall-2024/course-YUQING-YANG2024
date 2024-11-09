#get p-distance for every pair of strings in a collection

import unittest
"""
from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix
class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        self.assertEqual(.4, get_p_distance(['T','T','T','C','C','A','T','T','T','A'], 
                                            ['G','A','T','T','C','A','T','T','T','C']))

    def test_get_p_distance_matrix(self):
        list1 = [['T','T','T','C','C','A','T','T','T','A'], 
                 ['G','A','T','T','C','A','T','T','T','C'], 
                 ['T','T','T','C','C','A','T','T','T','T'], 
                 ['G','T','T','C','C','A','T','T','T','A']]
        list2 = [[0.0, 0.4, 0.1, 0.1], 
                 [0.4, 0.0, 0.4, 0.3], 
                 [0.1, 0.4, 0.0, 0.2], 
                 [0.1, 0.3, 0.2, 0.0]]
        self.assertEqual(list2, get_p_distance_matrix(list1))
"""

#HW8
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory
class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        widget_name = "Widget1"
        quantity = 10
        widgets_dictionary = {}
        add_inventory(widgets_dictionary, widget_name, quantity)
        self.assertEqual({"Widget1":10}, widgets_dictionary)
       
        widgets_dictionary1 = {"Widget1":25}
        widget_name = "Widget1"
        quantity = 35
        add_inventory(widgets_dictionary1, widget_name, quantity)
        self.assertEqual({"Widget1":35}, widgets_dictionary1)

        widgets_dictionary2 = {"Widget1":-10}
        widget_name = "Widget1"
        quantity = 25
        add_inventory(widgets_dictionary2, widget_name, quantity)
        self.assertEqual({"Widget1":25}, widgets_dictionary2)

    def test_remove_inventory(self):
        key = "Widget1"
        quantity = 5
        widgets_dictionary = {}
        add_inventory(widgets_dictionary, key, quantity)
        
        key = "Widget2"
        quantity = 9
        add_inventory(widgets_dictionary, key, quantity)
        print(widgets_dictionary)

        remove_inventory(widgets_dictionary, "Widget1")
        print("the length of widgets_dictionary is: ", len(widgets_dictionary))
        print("widgets_dictionary is: ", widgets_dictionary)
 