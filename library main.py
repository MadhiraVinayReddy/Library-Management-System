import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        # UI components
        self.label = tk.Label(root, text="Upload a CSV File with Library Data")
        self.label.pack(pady=10)

        self.upload_button = tk.Button(root, text="Browse File", command=self.browse_file)
        self.upload_button.pack(pady=5)

        self.summary_button = tk.Button(root, text="Show Summary", command=self.show_summary)
        self.summary_button.pack(pady=5)

        self.bar_chart_button = tk.Button(root, text="Show Bar Graph by Genre", command=self.show_bar_graph)
        self.bar_chart_button.pack(pady=5)

        self.pie_chart_button = tk.Button(root, text="Show Pie Chart by Genre", command=self.show_pie_chart)
        self.pie_chart_button.pack(pady=5)

        self.filepath = None
        self.library_data = None

    def browse_file(self):
        # Open file dialog to select a CSV file
        self.filepath = filedialog.askopenfilename(
            title="Open CSV File",
            filetypes=[("CSV Files", "*.csv")]
        )
        if self.filepath:
            self.label.config(text=f"Selected File: {self.filepath}")
            try:
                # Attempt to read the CSV file
                self.library_data = pd.read_csv(self.filepath, on_bad_lines='warn')
                
                # Print column names for debugging
                print("Columns in the CSV file:", self.library_data.columns.tolist())
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read CSV file: {e}")

    def show_summary(self):
        if self.library_data is None:
            messagebox.showerror("Error", "Please select a file first!")
            return

        # Ensure necessary columns exist
        if 'Title' not in self.library_data.columns or 'Genre' not in self.library_data.columns or 'Author' not in self.library_data.columns:
            messagebox.showerror("Error", "'Title', 'Genre', or 'Author' column not found in the CSV file.")
            return
        
        # Display summary statistics
        total_books = len(self.library_data)
        unique_genres = self.library_data['Genre'].nunique()
        unique_authors = self.library_data['Author'].nunique()
        
        summary_text = (
            f"Total Books: {total_books}\n"
            f"Unique Genres: {unique_genres}\n"
            f"Unique Authors: {unique_authors}"
        )

        messagebox.showinfo("Library Summary", summary_text)

    def show_bar_graph(self):
        if self.library_data is None:
            messagebox.showerror("Error", "Please select a file first!")
            return

        # Ensure 'Genre' column exists
        if 'Genre' not in self.library_data.columns:
            messagebox.showerror("Error", "'Genre' column not found in the CSV file.")
            return
        
        # Count the number of books by genre
        genre_counts = self.library_data['Genre'].value_counts()

        # Plot the bar graph
        plt.figure(figsize=(10, 6))
        genre_counts.plot(kind='bar', color='lightblue')
        plt.title('Number of Books by Genre')
        plt.xlabel('Genre')
        plt.ylabel('Number of Books')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Display the plot
        plt.show()

    def show_pie_chart(self):
        if self.library_data is None:
            messagebox.showerror("Error", "Please select a file first!")
            return

        # Ensure 'Genre' column exists
        if 'Genre' not in self.library_data.columns:
            messagebox.showerror("Error", "'Genre' column not found in the CSV file.")
            return
        
        # Count the number of books by genre
        genre_counts = self.library_data['Genre'].value_counts()

        # Plot the pie chart
        plt.figure(figsize=(8, 8))
        genre_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Book Distribution by Genre')
        plt.ylabel('')  # Remove y-label

        # Display the plot
        plt.show()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
    