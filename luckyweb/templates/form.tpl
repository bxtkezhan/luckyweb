<form action="{{ action }}" method="{{ method }}" enctype="{{ enctype }}">
  {% for group in groups %}
    {% if group.row %}
  <div class="form-group row">
    <label class="col-2 col-form-label">{{ group.label }}</label>
    <input type="{{ group.type }}" class="form-control col-10" placeholder="{{ group.placeholder }}" name="{{ group.name }}" step="any">
	{% else %}
  <div class="form-group">
    <label>{{ group.label }}</label>
    <input type="{{ group.type }}" class="form-control" placeholder="{{ group.placeholder }}" name="{{ group.name }}" step="any">
	{% endif %}
	{% if group.text %}
    <small class="form-text text-muted">{{ group.text }}</small>
	{% endif %}
  </div>
  {% endfor %}
  <button type="submit" class="btn btn-primary">{{ submit_text }}</button>
</form>
