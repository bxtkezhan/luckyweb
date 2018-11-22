<div class="table-responsive">
  <table class="table {{ _class }}">
    <thead>
  	<tr>
      {% for column in array[0] %}
  	  <th>{{ column }}</th>
	  {% endfor %}
  	</tr>
    </thead>
    <tbody>
	{% for line in array[1:] %}
  	<tr>
	  {% for item in line %}
  	  <td>{{ item }}</td>
	  {% endfor %}
  	</tr>
	{% endfor %}
    </tbody>
  </table>
</div>
