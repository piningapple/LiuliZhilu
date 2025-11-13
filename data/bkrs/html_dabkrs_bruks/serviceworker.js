'use strict';
const CACHE_NAME = 'HTML_v2.0:250314_dabkrs_dabruks';
try {
	self.addEventListener('install', function(event) {
		try {
			event.waitUntil((async function() {
				try {
					const cache = await caches.open(CACHE_NAME);
					
					
					// serviceworker.js должен располагаться в одном каталоге с *.html
					// Если изменяется имя и расположение *.html, также изменить по примеру:
					// https://site.rf/public/dict.html  ->  cache.addAll(['/public/dict.html']);

					cache.addAll(['/HTML/dabkrs_dabruks/dabkrs_dabruks.html']);
					
					
				} catch (er) {}
			})());
		} catch (er) {}
	});
	self.addEventListener('fetch', function(event) {
		try {
			event.respondWith((async function() {
				try {
					const cache = await caches.open(CACHE_NAME);
					const cachedResponse = await cache.match(event.request);
					if(cachedResponse) return cachedResponse;
					else {
						const fetchResponse = await fetch(event.request);
						cache.put(event.request, fetchResponse.clone());
						return fetchResponse;
					}
				} catch (er) {}
			})());
		} catch (er) {}
	});
} catch (er) {}
