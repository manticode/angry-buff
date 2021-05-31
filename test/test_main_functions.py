import unittest
import app


class TestCreateGroups(unittest.TestCase):
    group_size_8 = [1, 2, 3, 4, 5, 6, 7, 8]
    group_size_5 = [1, 2, 3, 4, 5]
    group_size_1 = [1]

    def test_size_5(self):
        self.test_result = app.create_groups(5)
        self.assertEqual(self.group_size_5, self.test_result)

    def test_size_1(self):
        self.test_result = app.create_groups(1)
        self.assertEqual(self.group_size_1, self.test_result)

    def test_size_8(self):
        self.test_result = app.create_groups(8)
        self.assertEqual(self.group_size_8, self.test_result)


class TestPriestFunction(unittest.TestCase):
    priests_list_13 = ["Necole", "Meghann", "Warren", "Ehtel", "Tonita", "Savanna", "Evalyn", "Kathlyn", "Mitchell",
                       "Hildegard", "Shirleen", "Allen", "Vincenzo"]
    priests_list_8 = ["Necole", "Meghann", "Warren", "Ehtel", "Tonita", "Savanna", "Evalyn", "Kathlyn"]
    priests_list_5 = ["Necole", "Meghann", "Warren", "Ehtel", "Tonita"]
    priests_list_3 = ["Leondréa", "Somnii", "Yoraint"]
    group_size_8 = [1, 2, 3, 4, 5, 6, 7, 8]
    group_size_5 = [1, 2, 3, 4, 5]
    group_size_1 = [1]
    result_13 = [{'priest': 'Necole', 'groups_assigned': [1]}, {'priest': 'Meghann', 'groups_assigned': [2]},
                 {'priest': 'Warren', 'groups_assigned': [3]}, {'priest': 'Ehtel', 'groups_assigned': [4]},
                 {'priest': 'Tonita', 'groups_assigned': [5]}, {'priest': 'Savanna', 'groups_assigned': [6]},
                 {'priest': 'Evalyn', 'groups_assigned': [7]}, {'priest': 'Kathlyn', 'groups_assigned': [8]},
                 {'priest': 'Mitchell', 'groups_assigned': []}, {'priest': 'Hildegard', 'groups_assigned': []},
                 {'priest': 'Shirleen', 'groups_assigned': []}, {'priest': 'Allen', 'groups_assigned': []},
                 {'priest': 'Vincenzo', 'groups_assigned': []}]

    result_8 = [{'priest': 'Necole', 'groups_assigned': [1]}, {'priest': 'Meghann', 'groups_assigned': [2]},
                {'priest': 'Warren', 'groups_assigned': [3]}, {'priest': 'Ehtel', 'groups_assigned': [4]},
                {'priest': 'Tonita', 'groups_assigned': [5]}, {'priest': 'Savanna', 'groups_assigned': [6]},
                {'priest': 'Evalyn', 'groups_assigned': [7]}, {'priest': 'Kathlyn', 'groups_assigned': [8]}]
    result_5 = [{'priest': 'Necole', 'groups_assigned': [1, 2]}, {'priest': 'Meghann', 'groups_assigned': [3, 4]},
                {'priest': 'Warren', 'groups_assigned': [5, 6]}, {'priest': 'Ehtel', 'groups_assigned': [7]},
                {'priest': 'Tonita', 'groups_assigned': [8]}]
    result_3 = [{'priest': 'Leondréa', 'groups_assigned': [1, 2, 3]},
                {'priest': 'Somnii', 'groups_assigned': [4, 5, 6]},
                {'priest': 'Yoraint', 'groups_assigned': [7, 8]}]

    def test_8_priest_8_group(self):
        """ Test case identifies 8 priests for a full raid, only makes sense to assign 1 group per priest. """
        self.test_result = app.construct_assignments(self.priests_list_8, self.group_size_8)
        self.assertEqual(self.result_8, self.test_result)

    def test_5_priest_8_group(self):
        """ Test case identifies 5 priests for a full raid. 3 priests will have two group assignments. """
        self.test_result = app.construct_assignments(self.priests_list_5, self.group_size_8)
        self.assertEqual(self.result_5, self.test_result)

    def test_3_priest_8_group(self):
        """ Test case identifies 3 priests for a full raid. 2 priests will have three group assignments. """
        self.test_result = app.construct_assignments(self.priests_list_3, self.group_size_8)
        self.assertEqual(self.result_3, self.test_result)

    def test_1_priest_8_group(self):
        """ Test case identifies 1 priest for a full raid. Will burn lots of candles. """
        pass

    def test_13_priest_8_group(self):
        """ Test case identifies 13 priests for a raid size of 8 groups. Only 8 priests will have assignments. """
        self.test_result = app.construct_assignments(self.priests_list_13, self.group_size_8)

        self.assertListEqual(se, self.test_result)

    def something_else(self):
        """"""


if __name__ == '__main__':
    unittest.main()
