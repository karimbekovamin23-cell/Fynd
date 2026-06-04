self.addEventListener('push', function(event) {
    if (!event.data) return;
    var data = event.data.json();
    event.waitUntil(
        self.registration.showNotification(data.title || 'FYND', {
            body: data.body || '',
            icon: '/static/icon-192.png',
            badge: '/static/icon-72.png',
            data: { url: data.url || '/' },
            vibrate: [200, 100, 200],
        })
    );
});

self.addEventListener('notificationclick', function(event) {
    event.notification.close();
    var url = event.notification.data.url;
    event.waitUntil(
        clients.matchAll({ type: 'window', includeUncontrolled: true }).then(function(list) {
            for (var i = 0; i < list.length; i++) {
                if (list[i].url.indexOf(url) !== -1 && 'focus' in list[i]) {
                    return list[i].focus();
                }
            }
            return clients.openWindow(url);
        })
    );
});
