<div class="list-group {{ _class }}">
  {% for item in _list %}
  <a href="{{ item.href }}" class="list-group-item {{ item._class }}" >{{ item.text }}</a>
  {% endfor %}
</div>
