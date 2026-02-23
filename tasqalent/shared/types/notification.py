from dataclasses import dataclass
from typing import Any

from tasqalent.shared.constants.notification import (
    NotificationChannel,
    NotificationType,
    NotificationUrgency
)

@dataclass
class NotificationPayload:
    user_id: str
    notification_type: NotificationType
    channel: NotificationChannel
    urgency: NotificationUrgency
    title: str
    body: str
    payload: dict[str, Any] | None = None