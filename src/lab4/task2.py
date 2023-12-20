import typing as tp


class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def transform_to_text(self):
        return f"{self.name} ({self.age})"


class Group:
    def __init__(self, min_age: int, max_age: int | None) -> None:
        self.min_age = min_age
        self.max_age = max_age
        self.users: tp.List[User] = []

    def is_user_can_join(self, user: User):
        if user.age < self.min_age:
            return False

        if self.max_age and user.age > self.max_age:
            return False

        return True

    def add_user(self, user: User):
        self.users.append(user)
        self.users.sort(key=lambda x: (-x.age, x.name))

    def transform_to_text(self):
        if len(self.users) == 0:
            return None

        users_text = ", ".join([i.transform_to_text() for i in self.users])
        prefix = ""

        if self.max_age is None:
            prefix = f"{self.min_age}+"
        else:
            prefix = f"{self.min_age}-{self.max_age}"

        return f"{prefix}: {users_text}"


def main() -> None:
    groups_nums: tp.List[tp.Any] = (
        [-1] + list(map(int, input("Введи все возрастные группы: ").split())) + [None]
    )

    groups = list(
        reversed(
            [
                Group(groups_nums[i] + 1, groups_nums[i + 1])
                for i in range(len(groups_nums) - 1)
            ]
        )
    )

    while True:
        line = input()
        if line == "END":
            break

        name, age = line.split(",")
        user = User(name, int(age))

        for group in groups:
            if group.is_user_can_join(user):
                group.add_user(user)
                break

    for group in groups:
        text = group.transform_to_text()
        if text:
            print(text)


if __name__ == "__main__":
    main()
