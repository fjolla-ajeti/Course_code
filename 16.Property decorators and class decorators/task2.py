#Task2

#Implement 2 classes, the first one is the Boss and the second one is the Worker.

#Worker has a property boss, and its value must be an instance of Boss.

#You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!

#You can refactor the existing code.

#id_ - is just a random unique integer


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Only instances of Worker can be added to the workers list")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            if self._boss:
                self._boss.workers.remove(self)
            self._boss = new_boss

            new_boss.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of Boss class")

boss1 = Boss(1, "Alex", "ABC Tech")
boss2 = Boss(2, "John", "XYZ Tech")

worker1 = Worker(101, "Alice", "ABC Tech", boss1)
worker2 = Worker(102, "Erza", "ABC Tech", boss1)

worker1.boss = boss2