from enum import Enum

class NotificationType(Enum):
    NEW_MESSAGE = 'new_message'
    ORDER_UPDATE = 'order_update'
    GIG_APPROVAL = 'gig_approval'
    SYSTEM_EVENT = 'system_event'

class NotificationChannel(Enum):
    EMAIL = 'email'
    PUSH = 'push'
    IN_APP = 'in_app'

class NotificationUrgency(Enum):
    CRITICAL = 'critical'
    NORMAL = 'normal'
    