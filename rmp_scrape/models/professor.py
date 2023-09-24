class Professor:
    """
    This class represents a professor
    """
    __name = None
    __department = None
    __rating = None
    __num_ratings = None
    __would_take_again_pct = None
    __level_of_difficulty = None

    def __init__(self):
        pass

    def __int__(self, name, department, rating, num_ratings, would_take_again_pct, level_of_difficulty):
        self.name = name
        self.department = department
        self.rating = rating
        self.num_ratings = num_ratings
        self.would_take_again_pct = would_take_again_pct
        self.level_of_difficulty = level_of_difficulty

    def get_name(self):
        return self.name

    def get_department(self):
        return self.department

    def get_rating(self):
        return self.rating

    def get_num_ratings(self):
        return self.num_ratings

    def get_would_take_again_pct(self):
        return self.would_take_again_pct

    def get_level_of_difficulty(self):
        return self.level_of_difficulty
