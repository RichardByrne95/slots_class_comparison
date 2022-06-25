import timeit
from decimal import Decimal
from functools import partial
from slots_class import Person, PersonSlots


def get_set_delete(person):
    person.address = "123 Main St"
    _ = person.address
    del person.address


def main():
    improvements = []
    iterations = 100
    i = 0

    while i < iterations:
        person = Person("John", "321 Side Street", 32)
        person_slots = PersonSlots("John", "321 Side Street", 32)
        no_slots = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
        slots = min(
            timeit.repeat(partial(get_set_delete, person_slots), number=1000000)
        )
        improvement = Decimal((no_slots - slots) / no_slots)
        improvements.append(improvement)
        i += 1

    average_improvement = Decimal((sum(improvements) / iterations) * 100).quantize(Decimal(".01"))
    print(f"Average improvement of {iterations} iteration(s): {average_improvement}%")


if __name__ == "__main__":
    main()
