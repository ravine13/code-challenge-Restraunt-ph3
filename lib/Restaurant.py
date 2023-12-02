class Restaurant:
    
    def __init__(self, name):
        self._name = name
        self.reviews = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        print("Restaurant name cannot be changed.")

    def add_review(self,review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews
    
    def get_customers(self):
        return list(set(review.customer for review in self.reviews))

