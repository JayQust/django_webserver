from datetime import datetime


class InMemoryPostsRepo:
    def __init__(self):
        self.next_id = 1
        self.by_id = {}

    def get_all(self):
        return tuple(self.by_id.values())

    def get_by_id(self, id):
        return self.by_id.get(id, None)

    def get_by_username(self, username):
        result = []
        for val in self.by_id.values():
            if val.author.username == username:
                result.append(val)
        return tuple(result)

    def get_by_category(self, category):
        result = []
        for val in self.by_id.values():
            if val.author.category == category:
                result.append(val)
        return tuple(result)

    def request_create(self, post):
        post.id = self.next_id
        post.created = datetime.now()
        self.by_id[post.id] = post
        self.next_id += 1
        return post

    def request_delete(self, id, user):
        p = self.get_by_id(id)
        if not p:
            return f"post does not exist for id: {id}"
        if p.autjor.id != user.id:
            return f"you are not author of this post id: {id}"
        del self.by_id[id]
        return None
