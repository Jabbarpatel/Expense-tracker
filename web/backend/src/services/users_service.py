from controllers.users_controller import UsersController


class UsersService:
    @staticmethod
    def get_all_users():
        controller = UsersController()
        users = controller.get_all_users()
        return users
