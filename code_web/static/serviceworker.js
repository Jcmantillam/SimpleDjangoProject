var staticCacheName = 'code_web-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/home',
        'about/',
        'https://drive.google.com/uc?id=1cbro_8_Cd2O0PoEfKnCbqBQhREThmgog',
        'https://drive.google.com/uc?id=1qt666hFGbie-UpjKTLmb580X8h-iQVTE',
        'https://drive.google.com/uc?id=1fKXUbI_QrZQukZdf_SMLneW5cSmCjOl6',
        'https://drive.google.com/uc?id=1Uf6N-bjOb_3uP4H4PYRNKsD0HYds88Yv',
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/home','about/','https://drive.google.com/uc?id=1cbro_8_Cd2O0PoEfKnCbqBQhREThmgog',
        'https://drive.google.com/uc?id=1qt666hFGbie-UpjKTLmb580X8h-iQVTE','https://drive.google.com/uc?id=1fKXUbI_QrZQukZdf_SMLneW5cSmCjOl6',
        'https://drive.google.com/uc?id=1Uf6N-bjOb_3uP4H4PYRNKsD0HYds88Yv'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});