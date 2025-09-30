const CACHE_NAME = 'lgs-test-v1.0';
const urlsToCache = [
    '/LGS_Test.html',
    '/LGS_Test_Standalone.html',
    '/manifest.json',
    '/embedded_excel_data.js',
    // CDN kaynakları için offline fallback (opsiyonel)
    'https://cdn.tailwindcss.com',
    'https://unpkg.com/react@18/umd/react.production.min.js',
    'https://unpkg.com/react-dom@18/umd/react-dom.production.min.js'
];

// Install event - cache resources
self.addEventListener('install', event => {
    console.log('LGS Test Service Worker: Installing...');
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('LGS Test Service Worker: Caching files');
                return cache.addAll(urlsToCache);
            })
            .then(() => {
                console.log('LGS Test Service Worker: Installation complete');
                return self.skipWaiting();
            })
            .catch(error => {
                console.error('LGS Test Service Worker: Installation failed', error);
            })
    );
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
    console.log('LGS Test Service Worker: Activating...');
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('LGS Test Service Worker: Deleting old cache', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => {
            console.log('LGS Test Service Worker: Activation complete');
            return self.clients.claim();
        })
    );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', event => {
    // Skip non-GET requests
    if (event.request.method !== 'GET') {
        return;
    }

    // Skip Chrome extension requests
    if (event.request.url.startsWith('chrome-extension://')) {
        return;
    }

    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Return cached version or fetch from network
                if (response) {
                    console.log('LGS Test Service Worker: Serving from cache', event.request.url);
                    return response;
                }

                console.log('LGS Test Service Worker: Fetching from network', event.request.url);
                return fetch(event.request).then(response => {
                    // Don't cache non-successful responses
                    if (!response || response.status !== 200 || response.type !== 'basic') {
                        return response;
                    }

                    // Clone the response for caching
                    const responseToCache = response.clone();
                    caches.open(CACHE_NAME)
                        .then(cache => {
                            cache.put(event.request, responseToCache);
                        });

                    return response;
                });
            })
            .catch(error => {
                console.error('LGS Test Service Worker: Fetch failed', error);
                
                // Return offline fallback for HTML requests
                if (event.request.destination === 'document') {
                    return caches.match('/LGS_Test.html');
                }
                
                // For other requests, just fail
                throw error;
            })
    );
});

// Background sync for test results (future feature)
self.addEventListener('sync', event => {
    if (event.tag === 'background-sync-test-results') {
        console.log('LGS Test Service Worker: Background sync triggered');
        // Future: sync test results to server
    }
});

// Push notifications (future feature)
self.addEventListener('push', event => {
    if (event.data) {
        const options = {
            body: event.data.text(),
            icon: '/icon-192x192.png',
            badge: '/icon-72x72.png',
            vibrate: [200, 100, 200],
            data: {
                dateOfArrival: Date.now(),
                primaryKey: 1
            },
            actions: [
                {
                    action: 'explore',
                    title: 'Test Çöz',
                    icon: '/icon-192x192.png'
                },
                {
                    action: 'close',
                    title: 'Kapat',
                    icon: '/icon-192x192.png'
                }
            ]
        };
        
        event.waitUntil(
            self.registration.showNotification('LGS Test Hatırlatması', options)
        );
    }
});