
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data generation for demonstration
def generate_sample_data():
    np.random.seed(0)
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    employees = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    data = []
    
    for date in dates:
        for employee in employees:
            hours_worked = np.random.randint(6, 10) if np.random.random() > 0.2 else 0  # 0 means absent
            # Check if hours worked is greater than 0 to decide arrival time
            if hours_worked > 0:
                arrival_times = pd.to_datetime(['09:00', '09:15', '09:30', '09:45'], format='%H:%M')
                arrival_time = np.random.choice(arrival_times, p=[0.5, 0.3, 0.1, 0.1])
            else:
                arrival_time = None
            data.append([date, employee, hours_worked, arrival_time])
    
    df = pd.DataFrame(data, columns=['Date', 'Employee', 'Hours Worked', 'Arrival Time'])
    return df

# Analysis Functions
def average_hours_worked(df):
    avg_hours = df.groupby('Employee')['Hours Worked'].mean()
    return avg_hours

def absenteeism_rate(df):
    absenteeism = df[df['Hours Worked'] == 0].groupby('Employee').size() / len(df['Date'].unique())
    return absenteeism

def late_arrivals(df):
    late_arrivals = df[df['Arrival Time'] > pd.to_datetime('09:15')].groupby('Employee').size()
    return late_arrivals

# Visualization Functions
def plot_average_hours(df):
    avg_hours = average_hours_worked(df)
    plt.figure(figsize=(8, 5))
    avg_hours.plot(kind='bar', color='skyblue')
    plt.title('Average Hours Worked per Employee')
    plt.ylabel('Average Hours')
    plt.xlabel('Employee')
    plt.tight_layout()
    plt.show()

def plot_absenteeism(df):
    absenteeism = absenteeism_rate(df)
    plt.figure(figsize=(8, 5))
    absenteeism.plot(kind='bar', color='lightcoral')
    plt.title('Absenteeism Rate per Employee')
    plt.ylabel('Absenteeism Rate')
    plt.xlabel('Employee')
    plt.tight_layout()
    plt.show()

def plot_late_arrivals(df):
    late_arrivals = late_arrivals(df)
    plt.figure(figsize=(8, 5))
    late_arrivals.plot(kind='bar', color='lightgreen')
    plt.title('Late Arrivals per Employee')
    plt.ylabel('Number of Late Arrivals')
    plt.xlabel('Employee')
    plt.tight_layout()
    plt.show()

def plot_heatmap(df):
    heatmap_data = df.pivot_table(index='Date', columns='Employee', values='Hours Worked', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='g', cbar_kws={'label': 'Hours Worked'})
    plt.title('Work Hours Heatmap')
    plt.tight_layout()
    plt.show()

# GUI Functions
def display_average_hours():
    avg_hours = average_hours_worked(df)
    messagebox.showinfo("Average Hours Worked", avg_hours.to_string())

def display_absenteeism():
    absenteeism = absenteeism_rate(df)
    messagebox.showinfo("Absenteeism Rate", absenteeism.to_string())

def display_late_arrivals():
    late_arrivals_stat = late_arrivals(df)
    messagebox.showinfo("Late Arrivals", late_arrivals_stat.to_string())

def display_heatmap():
    plot_heatmap(df)

def display_plots():
    plot_average_hours(df)
    plot_absenteeism(df)
    plot_late_arrivals(df)

# Setting up the Tkinter GUI
def run_gui():
    root = tk.Tk()
    root.title("Employee Work Pattern Analysis")

    tk.Label(root, text="Employee Work Pattern Analysis", font=("Helvetica", 16)).pack(pady=20)

    tk.Button(root, text="Display Average Hours Worked", width=30, command=display_average_hours).pack(pady=10)
    tk.Button(root, text="Display Absenteeism Rate", width=30, command=display_absenteeism).pack(pady=10)
    tk.Button(root, text="Display Late Arrivals", width=30, command=display_late_arrivals).pack(pady=10)
    tk.Button(root, text="Display All Visuals", width=30, command=display_plots).pack(pady=10)
    tk.Button(root, text="Show Work Hours Heatmap", width=30, command=display_heatmap).pack(pady=10)

    root.mainloop()

# Main Program
if __name__ == "__main__":
    # Load data
    df = generate_sample_data()

    # Run the GUI
    run_gui()
