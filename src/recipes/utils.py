
from io import BytesIO
import base64
import matplotlib
matplotlib.use('agg')  # Use the 'agg' backend
import matplotlib.pyplot as plt

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_chart(chart_type, data, **kwargs):
    if chart_type == '#1':
        plt.bar(data['name'], data['difficulty_level_choices'])
    elif chart_type == '#2':
        labels = data['category_choices']
        category_counts = {category: data['category_choices'].count(category) for category in labels}
        plt.pie(category_counts.values(), labels=category_counts.keys(), autopct='%1.1f%%')
    elif chart_type == '#3':
        plt.plot(data['name'], data['cooking_time'])
    else:
        return None

    # Save chart to bytes buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Encode image to base64
    return base64.b64encode(buf.read()).decode('utf-8')
