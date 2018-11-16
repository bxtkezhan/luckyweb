<div class="py-{{ args.py }}">
  <div class="container-fluid">
    <div class="row">
      {% for i in range(args.variable|length) %}
	    {% if args.cols_num|length > i %}
        <div class="col-sm-{{ args.cols_num[i] }}">
  		  {{ args.variable[i] }}
  	    </div>
		{% else %}
        <div class="col-sm">
  		  {{ args.variable[i] }}
  	    </div>
		{% endif %}
  	  {% endfor %}
    </div>
  </div>
</div>
