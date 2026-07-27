import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_how_it_works():
    plt.figure(figsize=(15, 3.5), dpi=300)
    plt.xkcd(scale=1.1, length=100, randomness=2)
    
    ax = plt.gca()
    ax.set_xlim(0, 115)
    ax.set_ylim(0, 35)
    ax.axis('off')
    
    steps = [
        (10, 18, "1. TRIGGER", "Daily at\n8:00 AM"),
        (28, 18, "2. FETCH", "Google RSS &\nHacker News"),
        (46, 18, "3. FILTER", "Deduplicate &\nkeep top 15"),
        (64, 18, "4. AI PARSER", "Gemini Outputs\nStructured JSON"),
        (82, 18, "5. TEMPLATE", "Code Node Builds\nHTML Email"),
        (100, 18, "6. DELIVER", "HTML Digest\nto Gmail")
    ]
    
    for x, y, label, sublabel in steps:
        rect = patches.FancyBboxPatch(
            (x - 7.5, y - 10), 15, 20, 
            boxstyle="round,pad=0.3", 
            fc="white", ec="black", lw=1.5
        )
        ax.add_patch(rect)
        plt.text(x, y + 2, label, ha="center", va="center", weight="bold", fontsize=9)
        plt.text(x, y - 4, sublabel, ha="center", va="center", fontsize=7.5, color="#444")
        
    for i in range(len(steps) - 1):
        x1, y1 = steps[i][0] + 8, steps[i][1]
        x2, y2 = steps[i+1][0] - 8, steps[i+1][1]
        ax.annotate(
            "", xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(arrowstyle="->", lw=1.5, color="black", 
                            connectionstyle="arc3,rad=0.1")
        )
        
    plt.title("HOW IT WORKS - AI AGENT PIPELINE", fontsize=12, weight="bold", pad=15)
    plt.tight_layout()
    plt.savefig("assets/how_it_works_sketch.png", bbox_inches='tight', transparent=True)
    plt.close()

def generate_system_architecture():
    plt.figure(figsize=(11, 9.5), dpi=300)
    plt.xkcd(scale=1.1, length=100, randomness=2)
    
    ax = plt.gca()
    ax.set_xlim(0, 100)
    ax.set_ylim(-5, 100)
    ax.axis('off')
    
    # Draw Alarm Cron Trigger
    ax.add_patch(patches.FancyBboxPatch((40, 84), 20, 10, boxstyle="round,pad=0.3", fc="white", ec="black", lw=1.5))
    plt.text(50, 91, "Cron Trigger", ha="center", va="center", weight="bold", fontsize=11)
    plt.text(50, 87, "8:00 AM Daily", ha="center", va="center", fontsize=9, color="#555")
    
    # Left Source: Google News
    ax.add_patch(patches.FancyBboxPatch((15, 62), 26, 12, boxstyle="round,pad=0.3", fc="white", ec="black", lw=1.5))
    plt.text(28, 70, "Google News RSS", ha="center", va="center", weight="bold", fontsize=10)
    plt.text(28, 65, "Scrapes AI & Agentic tags", ha="center", va="center", fontsize=8, color="#555")
    
    # Right Source: Hacker News
    ax.add_patch(patches.FancyBboxPatch((59, 62), 26, 12, boxstyle="round,pad=0.3", fc="white", ec="black", lw=1.5))
    plt.text(72, 70, "Hacker News API", ha="center", va="center", weight="bold", fontsize=10)
    plt.text(72, 65, "Algolia search: 'AI agent'", ha="center", va="center", fontsize=8, color="#555")
    
    # Merge, Deduplicate & Filter
    ax.add_patch(patches.FancyBboxPatch((25, 38), 50, 16, boxstyle="round,pad=0.3", fc="white", ec="black", lw=1.5))
    plt.text(50, 50, "Merge, Deduplicate & Filter", ha="center", va="center", weight="bold", fontsize=11)
    plt.text(50, 45, "• Combines feeds   • Filters duplicates (static data)\n• Checks 24h window   • Saves top 15 stories", ha="center", va="center", fontsize=8.5, color="#444")
    
    # count > 0
    diamond_x = [50, 60, 50, 40, 50]
    diamond_y = [32, 26, 20, 26, 32]
    plt.plot(diamond_x, diamond_y, color='black', lw=1.5)
    plt.text(50, 26, "count > 0?", ha="center", va="center", weight="bold", fontsize=9)
    
    # Gemini AI Box (JSON)
    ax.add_patch(patches.FancyBboxPatch((5, 2), 26, 12, boxstyle="round,pad=0.3", fc="white", ec="black", lw=1.5))
    plt.text(18, 10, "Gemini LLM", ha="center", va="center", weight="bold", fontsize=10)
    plt.text(18, 5, "Extracts Structured\nJSON Schema", ha="center", va="center", fontsize=8, color="#555")
    
    # HTML Templating Box
    ax.add_patch(patches.FancyBboxPatch((37, 2), 26, 12, boxstyle="round,pad=0.3", fc="white", ec="black", lw=1.5))
    plt.text(50, 10, "JS Code Node", ha="center", va="center", weight="bold", fontsize=10)
    plt.text(50, 5, "Parses JSON & Builds\nHTML Template", ha="center", va="center", fontsize=8, color="#555")

    # Gmail Box
    ax.add_patch(patches.FancyBboxPatch((69, 2), 26, 12, boxstyle="round,pad=0.3", fc="white", ec="black", lw=1.5))
    plt.text(82, 10, "Gmail Delivery", ha="center", va="center", weight="bold", fontsize=10)
    plt.text(82, 5, "Sends Final Digest\nto Inbox", ha="center", va="center", fontsize=8, color="#555")
    
    # Arrows
    ax.annotate("", xy=(28, 75), xytext=(40, 89), arrowprops=dict(arrowstyle="->", lw=1.5, connectionstyle="arc3,rad=-0.1"))
    ax.annotate("", xy=(72, 75), xytext=(60, 89), arrowprops=dict(arrowstyle="->", lw=1.5, connectionstyle="arc3,rad=0.1"))
    ax.annotate("", xy=(35, 55), xytext=(28, 61), arrowprops=dict(arrowstyle="->", lw=1.5, connectionstyle="arc3,rad=0.1"))
    ax.annotate("", xy=(65, 55), xytext=(72, 61), arrowprops=dict(arrowstyle="->", lw=1.5, connectionstyle="arc3,rad=-0.1"))
    ax.annotate("", xy=(50, 33), xytext=(50, 37), arrowprops=dict(arrowstyle="->", lw=1.5))
    
    # Diamond to Gemini
    ax.annotate("", xy=(20, 15), xytext=(40, 26), arrowprops=dict(arrowstyle="->", lw=1.5, connectionstyle="arc3,rad=0.1"))
    plt.text(27, 21, "Yes", fontsize=8)
    
    # Gemini to Code Node
    ax.annotate("", xy=(36, 8), xytext=(32, 8), arrowprops=dict(arrowstyle="->", lw=1.5))
    
    # Code Node to Gmail
    ax.annotate("", xy=(68, 8), xytext=(64, 8), arrowprops=dict(arrowstyle="->", lw=1.5))
    
    # Diamond to STOP
    ax.annotate("", xy=(80, 26), xytext=(60, 26), arrowprops=dict(arrowstyle="->", lw=1.5))
    plt.text(70, 28, "No", fontsize=8)
    plt.text(85, 26, "STOP", ha="center", va="center", weight="bold", color="red", fontsize=10)
    
    plt.title("N8N WORKFLOW SYSTEM ARCHITECTURE", fontsize=13, weight="bold", pad=20)
    plt.tight_layout()
    plt.savefig("assets/architecture_sketch.png", bbox_inches='tight', transparent=True)
    plt.close()

if __name__ == "__main__":
    import os
    if not os.path.exists("assets"):
        os.makedirs("assets")
    generate_how_it_works()
    generate_system_architecture()
    print("Diagrams generated successfully!")
