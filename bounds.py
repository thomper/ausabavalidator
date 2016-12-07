from util import pluralise


class Bounds:
    """A range."""
    def __init__(self, start, end):
        """
        start: inclusive
        end: exclusive
        """
        self.start = start
        self.end = end

    @property
    def display_tuple(self):
        """The bounds as users expect them: a closed rather than half-open interval, indexed from 1 rather than 0."""
        return self.start + 1, self.end

    @property
    def display_string(self):
        """self.display_tuple formatted for users."""
        return pluralise(self.display_tuple, str(self.start), '{}-{}'.format(self.start, self.end))

    def __iter__(self):
        return iter((self.start, self.end))

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '<Bounds: {}>'.format(self.display_string)
