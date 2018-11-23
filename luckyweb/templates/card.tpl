<div class="card">
  {% if header %}
  <div class="card-header" > {{ header }} </div>
  {% endif %}
  <div class="card-body">
    {% for item in variable %}
	{{ item }}
	{% endfor %}
  </div>
</div>
