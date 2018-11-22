<ul class="pagination" >
  {% for page in pages %}
    {% if page.active %}
  <li class="page-item active"> <a class="page-link" href="{{ page.href }}">{{ page.text }}</a> </li>
    {% else %}
	  {% if page.disabled %}
  <li class="page-item disabled"> <a class="page-link" href="{{ page.href }}">{{ page.text }}</a> </li>
      {% else %}
  <li class="page-item"> <a class="page-link" href="{{ page.href }}">{{ page.text }}</a> </li>
      {% endif %}
    {% endif %}
  {% endfor %}
</ul>
