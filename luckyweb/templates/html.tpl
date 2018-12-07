<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{{ title }}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {% for url in css_urls %}
  <link rel="stylesheet" href="{{ url }}">
  {% endfor %}
  {% for url in js_urls %}
  <script src="{{ url }}"></script>
  {% endfor %}
</head>
<body>
{% for item in variable %}
{{ item }}
{% endfor %}
</body>
</html>
