# utils/ui_state_manager.py
import json
import traceback
from PySide2.QtWidgets import QFileDialog, QMessageBox, QWidget, QSpinBox, QDoubleSpinBox, QComboBox, QLineEdit, QCheckBox
from PySide2.QtCore import QObject # For findChild, findChildren

def save_ui_state(main_window_instance):
    """Saves the current values of all relevant UI fields to a JSON file."""
    print("Save action triggered!")
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getSaveFileName(main_window_instance, "Save UI State", "",
                                              "JSON Files (*.json);;All Files (*)", options=options)
    if not fileName:
        print("Save cancelled.")
        return

    if not fileName.lower().endswith('.json'):
        fileName += '.json'
    
    print(f"Attempting to save UI state to: {fileName}")
    ui_state = {}
    try:
        all_widgets = main_window_instance.findChildren(QWidget)
        widgets_to_save = [w for w in all_widgets if isinstance(w, (QSpinBox, QDoubleSpinBox, QComboBox, QLineEdit, QCheckBox))]

        for widget in widgets_to_save:
            object_name = widget.objectName()
            if not object_name:
                print(f"Warning: Skipping widget of type {type(widget)} because it has no object name.")
                continue

            value = None
            if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                value = widget.value()
            elif isinstance(widget, QComboBox):
                value = widget.currentText()
            elif isinstance(widget, QLineEdit):
                value = widget.text()
            elif isinstance(widget, QCheckBox):
                value = widget.isChecked()
            
            if value is not None:
                ui_state[object_name] = value
            else:
                print(f"Warning: Could not determine value for widget {object_name} of type {type(widget)}")
        
        ui_state['__current_tab_index__'] = main_window_instance.ui.tabWidget.currentIndex()

        with open(fileName, 'w') as f:
            json.dump(ui_state, f, indent=4)

        print(f"UI state successfully saved to {fileName}")
        QMessageBox.information(main_window_instance, "Save Successful", f"UI state saved to:\n{fileName}")

    except Exception as e:
        print(f"Error saving UI state: {e}")
        detailed_error = traceback.format_exc()
        QMessageBox.critical(main_window_instance, "Save Error", f"Could not save UI state:\n{e}\n\nDetails:\n{detailed_error}")


def load_ui_state(main_window_instance):
    """Loads UI state from a selected JSON file."""
    print("Load action triggered!")
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getOpenFileName(main_window_instance, "Load UI State", "",
                                              "JSON Files (*.json);;All Files (*)", options=options)
    if not fileName:
        print("Load cancelled.")
        return
    
    print(f"Attempting to load UI state from: {fileName}")
    try:
        with open(fileName, 'r') as f:
            ui_state = json.load(f)

        for object_name, value in ui_state.items():
            if object_name == '__current_tab_index__':
                if isinstance(value, int) and 0 <= value < main_window_instance.ui.tabWidget.count():
                    main_window_instance.ui.tabWidget.setCurrentIndex(value)
                continue

            widget = main_window_instance.findChild(QObject, object_name)

            if widget:
                if isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                    try:
                        widget.setValue(float(value) if isinstance(widget, QDoubleSpinBox) else int(value))
                    except (TypeError, ValueError) as type_err:
                        print(f"Warning: Type mismatch for {object_name}. Expected number, got {type(value)}. Error: {type_err}")
                elif isinstance(widget, QComboBox):
                    index = widget.findText(str(value))
                    if index != -1:
                        widget.setCurrentIndex(index)
                    else:
                        print(f"Warning: Could not find text '{value}' in ComboBox '{object_name}'.")
                elif isinstance(widget, QLineEdit):
                    widget.setText(str(value))
                elif isinstance(widget, QCheckBox):
                    widget.setChecked(bool(value))
                else:
                    print(f"Widget {object_name} found, but its type ({type(widget)}) is not handled for loading.")
            else:
                print(f"Warning: Widget with object name '{object_name}' not found in the UI.")

        print(f"UI state successfully loaded from {fileName}")
        QMessageBox.information(main_window_instance, "Load Successful", f"UI state loaded from:\n{fileName}")

    except FileNotFoundError:
        print(f"Error: File not found - {fileName}")
        QMessageBox.critical(main_window_instance, "Load Error", f"File not found:\n{fileName}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON file - {fileName}. Error: {e}")
        QMessageBox.critical(main_window_instance, "Load Error", f"Could not parse JSON file:\n{fileName}\n\nError: {e}")
    except Exception as e:
        print(f"Error loading UI state: {e}")
        detailed_error = traceback.format_exc()
        QMessageBox.critical(main_window_instance, "Load Error", f"An unexpected error occurred while loading UI state:\n{e}\n\nDetails:\n{detailed_error}")