from appnexusclient.models.base import Base


class Deal(Base):

    obj_name = "deal"

    def set_buyer(self, id):
        self['buyer'] = {'id': id}
