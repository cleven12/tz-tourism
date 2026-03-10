from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from app.attractions.models import Attraction
from app.regions.models import Region
from app.blog.models import Article


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "Disallow: /api/schema/",
        "",
        "Sitemap: https://xenohuru.onrender.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def sitemap_xml(request):
    base_url = "https://xenohuru.onrender.com"
    urls = []

    # Static pages
    urls.append(f'<url><loc>{base_url}/api/docs/</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>')
    urls.append(f'<url><loc>{base_url}/api/v1/attractions/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>')
    urls.append(f'<url><loc>{base_url}/api/v1/regions/</loc><changefreq>weekly</changefreq><priority>0.9</priority></url>')
    urls.append(f'<url><loc>{base_url}/api/v1/blog/</loc><changefreq>daily</changefreq><priority>0.8</priority></url>')

    # Attractions
    for attraction in Attraction.objects.filter(is_active=True).values('slug', 'updated_at'):
        urls.append(
            f'<url>'
            f'<loc>{base_url}/api/v1/attractions/{attraction["slug"]}/</loc>'
            f'<lastmod>{attraction["updated_at"].strftime("%Y-%m-%d")}</lastmod>'
            f'<changefreq>weekly</changefreq>'
            f'<priority>0.9</priority>'
            f'</url>'
        )

    # Regions
    for region in Region.objects.all().values('slug', 'updated_at'):
        urls.append(
            f'<url>'
            f'<loc>{base_url}/api/v1/regions/{region["slug"]}/</loc>'
            f'<lastmod>{region["updated_at"].strftime("%Y-%m-%d")}</lastmod>'
            f'<changefreq>monthly</changefreq>'
            f'<priority>0.7</priority>'
            f'</url>'
        )

    # Blog articles
    for article in Article.objects.filter(is_published=True).values('slug', 'updated_at'):
        urls.append(
            f'<url>'
            f'<loc>{base_url}/api/v1/blog/{article["slug"]}/</loc>'
            f'<lastmod>{article["updated_at"].strftime("%Y-%m-%d")}</lastmod>'
            f'<changefreq>monthly</changefreq>'
            f'<priority>0.6</priority>'
            f'</url>'
        )

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += '\n'.join(urls)
    xml += '\n</urlset>'
    return HttpResponse(xml, content_type='application/xml')


def health_check(request):
    from django.conf import settings
    from app.regions.models import Region
    from app.attractions.models import Attraction
    db_path = str(settings.DATABASES['default']['NAME'])
    try:
        region_count = Region.objects.count()
        attraction_count = Attraction.objects.count()
        db_status = 'ok'
    except Exception as e:
        region_count = -1
        attraction_count = -1
        db_status = str(e)

    return JsonResponse({
        'status': 'ok',
        'timestamp': timezone.now().isoformat(),
        'service': 'Xenohuru API',
        'db_path': db_path,
        'db_status': db_status,
        'regions': region_count,
        'attractions': attraction_count,
    })
