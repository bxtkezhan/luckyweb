<form action="{{ action }}" method="{{ method }}" enctype="{{ enctype }}">
  {% for group in groups %}
  <div class="form-group">
    <label>{{ group.label }}</label>
    <input type="{{ group.type }}" class="form-control" placeholder="{{ group.placeholder }}" name="{{ group.name }}">
	{% if group.text %}
    <small class="form-text text-muted">{{ group.text }}</small>
	{% endif %}
  </div>
  {% endfor %}
  <button type="submit" class="btn btn-primary">{{ submit_text }}</button>
</form>
