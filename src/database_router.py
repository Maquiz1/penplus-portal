class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """Direct read operations to the appropriate database."""
        if model._meta.app_label == 'penplus':
            return 'penplus'
        elif model._meta.app_label == 'pedx':
            return 'pedx'
        elif model._meta.app_label == 'logbook':
            return 'logbook'
        return None

    def db_for_write(self, model, **hints):
        """Direct write operations to the appropriate database."""
        if model._meta.app_label == 'penplus':
            return 'penplus'
        elif model._meta.app_label == 'pedx':
            return 'pedx'
        elif model._meta.app_label == 'logbook':
            return 'logbook'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations only within the same database."""
        db_set = {'penplus', 'pedx', 'logbook'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure migrations are applied to the correct database."""
        if app_label == 'penplus':
            return db == 'penplus'
        elif app_label == 'pedx':
            return db == 'pedx'
        elif app_label == 'logbook':
            return db == 'logbook'
        return None