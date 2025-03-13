from nicegui import ui

ui.colors(
      primary='#842cbf',
      secondary='#a18720',
      accent='#4fa1c2',
      positive='#2cab20',
      negative='#ba1a2d',
      info='#cca8ed',
      warning='#f28d49'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: sets the color of the text to the 'positive' theme color
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4 underline")
        # text-negative: sets the color of the text to the 'negative' theme color

def convert2():
    try: 
        temp = float(temp_slider.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4 underline")

with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        # w-100: Set element width to be fixed at 100
        # p-6: Sets the padding of the element to 6px
        # shadow-xl: Sets a large shadow around the border of the element
        # mx-auto: Automatically sets the margin of the element so that it is centered on the screen
        # mt-10: Sets the margin from the top of the screen/container to 10px
        # rounded-xl: Sets a large border radius so that the container appears rounded
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: Sets the size of the text to a large '2xl' size
        # font-bold: Bolds the font of the text
        # text-accent: sets the color of the text to the 'accent' theme color
        # mb-4: sets the bottom/below margin to 4px
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
        # w-full: Sets the width of the element to 100% of the width of the container (excluding padding)
        # border: Gives an outside border to the elemetn 
        # rounded: Sets the border of the element to have rounded corners
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4 font-semibold text-secondary tracking-wide")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-4 px-8 rounded mx-auto")
        # text-white: Sets the text color to white
        # py-2: Sets the vertical padding of the element to 2px
        # px-4: Sets the horizontal padding of the element to 4px
        result_label = ui.label("").classes("text-lg mt-4")

    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        ui.label("Slider Selection").classes("text-xl font-bold text-accent mb-4")
        temp_slider = ui.slider(min=-50, max=200, value=50)
        ui.label().bind_text_from(temp_slider, 'value').classes("text-xl font-bold, mx-auto py-4")
        convert_button2 = ui.button("Convert", on_click=convert2).classes("text-white font-bold py-4 px-8 rounded mx-auto")

ui.run()