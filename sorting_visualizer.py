import customtkinter as ctk
import random
import time
import threading
from typing import List, Callable
import tkinter as tk

# CustomTkinter temasını ayarla
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SortingVisualizer:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Sıralama Algoritmaları Görselleştirici")
        self.root.geometry("1200x800")
        
        # Değişkenler
        self.array = []
        self.array_size = 50
        self.sorting_speed = 0.1
        self.is_sorting = False
        self.current_algorithm = "Bubble Sort"
        
        # Sıralama algoritmaları
        self.algorithms = {
            "Bubble Sort": self.bubble_sort,
            "Selection Sort": self.selection_sort,
            "Insertion Sort": self.insertion_sort,
            "Quick Sort": self.quick_sort,
            "Merge Sort": self.merge_sort,
            "Heap Sort": self.heap_sort,
            "Shell Sort": self.shell_sort,
            "Radix Sort": self.radix_sort
        }
        
        # Algoritma bilgileri
        self.algorithm_info = {
            "Bubble Sort": {
                "description": "Bubble Sort, en basit sıralama algoritmasıdır. Komşu elemanları karşılaştırarak sıralama yapar.",
                "how_it_works": "1. İlk elemandan başlayarak komşu elemanları karşılaştırır\n2. Eğer sol eleman sağ elemandan büyükse yer değiştirir\n3. Bu işlemi tüm liste sıralanana kadar tekrarlar",
                "complexity": "• Zaman Karmaşıklığı: O(n²)\n• Uzay Karmaşıklığı: O(1)\n• En İyi Durum: O(n)\n• En Kötü Durum: O(n²)",
                "advantages": "• Basit ve anlaşılır\n• Ekstra bellek gerektirmez\n• Küçük listeler için uygun",
                "disadvantages": "• Büyük listeler için çok yavaş\n• Verimsiz algoritma"
            },
            "Selection Sort": {
                "description": "Selection Sort, en küçük elemanı bulup başa taşıyarak sıralama yapar.",
                "how_it_works": "1. Listede en küçük elemanı bulur\n2. Bu elemanı listenin başına taşır\n3. Kalan elemanlarla işlemi tekrarlar",
                "complexity": "• Zaman Karmaşıklığı: O(n²)\n• Uzay Karmaşıklığı: O(1)\n• En İyi Durum: O(n²)\n• En Kötü Durum: O(n²)",
                "advantages": "• Basit implementasyon\n• Ekstra bellek gerektirmez\n• Yer değiştirme sayısı az",
                "disadvantages": "• Her durumda O(n²) karmaşıklık\n• Verimsiz algoritma"
            },
            "Insertion Sort": {
                "description": "Insertion Sort, elemanları tek tek alıp uygun pozisyona yerleştirerek sıralama yapar.",
                "how_it_works": "1. İkinci elemandan başlar\n2. Her elemanı önceki elemanlarla karşılaştırır\n3. Uygun pozisyona yerleştirir",
                "complexity": "• Zaman Karmaşıklığı: O(n²)\n• Uzay Karmaşıklığı: O(1)\n• En İyi Durum: O(n)\n• En Kötü Durum: O(n²)",
                "advantages": "• Küçük listeler için verimli\n• Neredeyse sıralı listeler için hızlı\n• Ekstra bellek gerektirmez",
                "disadvantages": "• Büyük listeler için yavaş\n• O(n²) ortalama karmaşıklık"
            },
            "Quick Sort": {
                "description": "Quick Sort, pivot eleman seçerek listeyi böler ve recursive olarak sıralama yapar.",
                "how_it_works": "1. Pivot eleman seçer (genellikle son eleman)\n2. Pivot'tan küçük elemanları sola, büyükleri sağa yerleştirir\n3. Alt listeleri recursive olarak sıralar",
                "complexity": "• Zaman Karmaşıklığı: O(n log n)\n• Uzay Karmaşıklığı: O(log n)\n• En İyi Durum: O(n log n)\n• En Kötü Durum: O(n²)",
                "advantages": "• Ortalama durumda çok hızlı\n• Yerinde sıralama\n• Cache dostu",
                "disadvantages": "• En kötü durumda O(n²)\n• Pivot seçimi kritik"
            },
            "Merge Sort": {
                "description": "Merge Sort, listeyi ikiye böler, sıralar ve birleştirerek sıralama yapar.",
                "how_it_works": "1. Listeyi ortadan ikiye böler\n2. Alt listeleri recursive olarak sıralar\n3. Sıralı alt listeleri birleştirir",
                "complexity": "• Zaman Karmaşıklığı: O(n log n)\n• Uzay Karmaşıklığı: O(n)\n• En İyi Durum: O(n log n)\n• En Kötü Durum: O(n log n)",
                "advantages": "• Kararlı performans\n• Her durumda O(n log n)\n• Büyük veri setleri için uygun",
                "disadvantages": "• Ekstra bellek gerektirir\n• Küçük listeler için aşırı",
                "stable": "Evet"
            },
            "Heap Sort": {
                "description": "Heap Sort, heap veri yapısını kullanarak sıralama yapar.",
                "how_it_works": "1. Listeyi max heap'e dönüştürür\n2. Root elemanı (en büyük) sona taşır\n3. Heap'i yeniden düzenler ve tekrarlar",
                "complexity": "• Zaman Karmaşıklığı: O(n log n)\n• Uzay Karmaşıklığı: O(1)\n• En İyi Durum: O(n log n)\n• En Kötü Durum: O(n log n)",
                "advantages": "• Her durumda O(n log n)\n• Ekstra bellek gerektirmez\n• Heap yapısı korunur",
                "disadvantages": "• Cache dostu değil\n• Küçük listeler için aşırı"
            },
            "Shell Sort": {
                "description": "Shell Sort, Insertion Sort'un geliştirilmiş versiyonudur. Gap kullanarak elemanları karşılaştırır.",
                "how_it_works": "1. Gap değeri ile elemanları gruplar\n2. Her grupta Insertion Sort uygular\n3. Gap değerini azaltarak tekrarlar",
                "complexity": "• Zaman Karmaşıklığı: O(n^1.5)\n• Uzay Karmaşıklığı: O(1)\n• En İyi Durum: O(n log n)\n• En Kötü Durum: O(n²)",
                "advantages": "• Insertion Sort'tan daha hızlı\n• Ekstra bellek gerektirmez\n• Orta boyutlu listeler için uygun",
                "disadvantages": "• Gap sequence kritik\n• Karmaşıklık analizi zor"
            },
            "Radix Sort": {
                "description": "Radix Sort, sayıları basamaklarına göre sıralama yapar.",
                "how_it_works": "1. En az anlamlı basamaktan başlar\n2. Her basamak için Counting Sort uygular\n3. Tüm basamaklar bitene kadar tekrarlar",
                "complexity": "• Zaman Karmaşıklığı: O(d(n+k))\n• Uzay Karmaşıklığı: O(n+k)\n• En İyi Durum: O(d(n+k))\n• En Kötü Durum: O(d(n+k))",
                "advantages": "• Sayısal veriler için çok hızlı\n• Kararlı performans\n• Büyük sayılar için uygun",
                "disadvantages": "• Sadece sayısal veriler için\n• Ekstra bellek gerektirir\n• d (basamak sayısı) kritik"
            }
        }
        
        self.setup_ui()
        self.generate_new_array()
    
    def setup_ui(self):
        # Ana frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Kontrol paneli
        control_frame = ctk.CTkFrame(main_frame)
        control_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        # Sol kontroller
        left_controls = ctk.CTkFrame(control_frame)
        left_controls.pack(side="left", padx=10, pady=10)
        
        # Algoritma seçimi
        ctk.CTkLabel(left_controls, text="Algoritma:").pack(side="left", padx=(0, 5))
        self.algorithm_var = ctk.StringVar(value="Bubble Sort")
        algorithm_menu = ctk.CTkOptionMenu(
            left_controls, 
            values=list(self.algorithms.keys()),
            variable=self.algorithm_var,
            command=self.on_algorithm_change
        )
        algorithm_menu.pack(side="left", padx=(0, 5))
        
        # Bilgi butonu
        self.info_btn = ctk.CTkButton(
            left_controls,
            text="ℹ",
            width=30,
            height=30,
            command=self.show_algorithm_info
        )
        self.info_btn.pack(side="left", padx=(0, 10))
        
        # Liste boyutu
        ctk.CTkLabel(left_controls, text="Liste Boyutu:").pack(side="left", padx=(0, 5))
        self.size_var = ctk.StringVar(value="50")
        size_menu = ctk.CTkOptionMenu(
            left_controls,
            values=["10", "25", "50", "100", "200"],
            variable=self.size_var,
            command=self.on_size_change
        )
        size_menu.pack(side="left", padx=(0, 10))
        
        # Hız ayarı
        ctk.CTkLabel(left_controls, text="Hız:").pack(side="left", padx=(0, 5))
        self.speed_var = ctk.StringVar(value="0.1")
        speed_menu = ctk.CTkOptionMenu(
            left_controls,
            values=["0.01", "0.05", "0.1", "0.2", "0.5"],
            variable=self.speed_var,
            command=self.on_speed_change
        )
        speed_menu.pack(side="left", padx=(0, 10))
        
        # Sağ kontroller
        right_controls = ctk.CTkFrame(control_frame)
        right_controls.pack(side="right", padx=10, pady=10)
        
        # Butonlar
        self.generate_btn = ctk.CTkButton(
            right_controls,
            text="Yeni Liste Oluştur",
            command=self.generate_new_array
        )
        self.generate_btn.pack(side="left", padx=(0, 10))
        
        self.sort_btn = ctk.CTkButton(
            right_controls,
            text="Sıralamayı Başlat",
            command=self.start_sorting
        )
        self.sort_btn.pack(side="left", padx=(0, 10))
        
        self.stop_btn = ctk.CTkButton(
            right_controls,
            text="Durdur",
            command=self.stop_sorting,
            state="disabled"
        )
        self.stop_btn.pack(side="left")
        
        # Görselleştirme alanı
        self.canvas_frame = ctk.CTkFrame(main_frame)
        self.canvas_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Canvas oluştur
        self.canvas = tk.Canvas(
            self.canvas_frame,
            bg="#2b2b2b",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)
        
        # Bilgi paneli
        info_frame = ctk.CTkFrame(main_frame)
        info_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        self.info_label = ctk.CTkLabel(
            info_frame,
            text="Hazır - Yeni liste oluşturun veya sıralamayı başlatın",
            font=("Arial", 12)
        )
        self.info_label.pack(pady=10)
    
    def on_algorithm_change(self, value):
        self.current_algorithm = value
    
    def on_size_change(self, value):
        self.array_size = int(value)
        self.generate_new_array()
    
    def on_speed_change(self, value):
        self.sorting_speed = float(value)
    
    def show_algorithm_info(self):
        """Seçilen algoritma hakkında bilgi modalını gösterir"""
        current_algo = self.current_algorithm
        if current_algo not in self.algorithm_info:
            return
        
        info = self.algorithm_info[current_algo]
        
        # Modal pencere oluştur
        modal = ctk.CTkToplevel(self.root)
        modal.title(f"{current_algo} - Algoritma Bilgisi")
        modal.geometry("600x700")
        modal.resizable(False, False)
        modal.transient(self.root)
        modal.grab_set()
        
        # Modal'ı ana pencereye göre ortala
        modal.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (600 // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (700 // 2)
        modal.geometry(f"600x700+{x}+{y}")
        
        # Ana frame
        main_frame = ctk.CTkFrame(modal)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Başlık
        header_frame = ctk.CTkFrame(main_frame)
        header_frame.pack(fill="x", padx=10, pady=(10, 20))
        
        title_label = ctk.CTkLabel(
            header_frame,
            text=current_algo,
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=10)
        
        # Scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(main_frame)
        scroll_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Açıklama
        desc_label = ctk.CTkLabel(
            scroll_frame,
            text="Açıklama:",
            font=("Arial", 14, "bold")
        )
        desc_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        desc_text = ctk.CTkLabel(
            scroll_frame,
            text=info["description"],
            font=("Arial", 12),
            wraplength=500
        )
        desc_text.pack(anchor="w", padx=10, pady=(0, 15))
        
        # Nasıl çalışır
        how_label = ctk.CTkLabel(
            scroll_frame,
            text="Nasıl Çalışır:",
            font=("Arial", 14, "bold")
        )
        how_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        how_text = ctk.CTkLabel(
            scroll_frame,
            text=info["how_it_works"],
            font=("Arial", 12),
            wraplength=500,
            justify="left"
        )
        how_text.pack(anchor="w", padx=10, pady=(0, 15))
        
        # Karmaşıklık
        complexity_label = ctk.CTkLabel(
            scroll_frame,
            text="Karmaşıklık Analizi:",
            font=("Arial", 14, "bold")
        )
        complexity_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        complexity_text = ctk.CTkLabel(
            scroll_frame,
            text=info["complexity"],
            font=("Arial", 12),
            wraplength=500,
            justify="left"
        )
        complexity_text.pack(anchor="w", padx=10, pady=(0, 15))
        
        # Avantajlar
        advantages_label = ctk.CTkLabel(
            scroll_frame,
            text="Avantajlar:",
            font=("Arial", 14, "bold")
        )
        advantages_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        advantages_text = ctk.CTkLabel(
            scroll_frame,
            text=info["advantages"],
            font=("Arial", 12),
            wraplength=500,
            justify="left"
        )
        advantages_text.pack(anchor="w", padx=10, pady=(0, 15))
        
        # Dezavantajlar
        disadvantages_label = ctk.CTkLabel(
            scroll_frame,
            text="Dezavantajlar:",
            font=("Arial", 14, "bold")
        )
        disadvantages_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        disadvantages_text = ctk.CTkLabel(
            scroll_frame,
            text=info["disadvantages"],
            font=("Arial", 12),
            wraplength=500,
            justify="left"
        )
        disadvantages_text.pack(anchor="w", padx=10, pady=(0, 15))
        
        # Kararlılık (varsa)
        if "stable" in info:
            stable_label = ctk.CTkLabel(
                scroll_frame,
                text="Kararlılık:",
                font=("Arial", 14, "bold")
            )
            stable_label.pack(anchor="w", padx=10, pady=(10, 5))
            
            stable_text = ctk.CTkLabel(
                scroll_frame,
                text=f"Bu algoritma kararlıdır: {info['stable']}",
                font=("Arial", 12),
                wraplength=500
            )
            stable_text.pack(anchor="w", padx=10, pady=(0, 15))
        
        # Alt bilgi
        footer_label = ctk.CTkLabel(
            scroll_frame,
            text="💡 İpucu: Farklı algoritmaları test ederek performans farklarını gözlemleyin!",
            font=("Arial", 11, "italic"),
            text_color="#74b9ff"
        )
        footer_label.pack(anchor="w", padx=10, pady=(20, 10))
    
    def generate_new_array(self):
        self.array = [random.randint(10, 400) for _ in range(self.array_size)]
        # Yeni liste için çubukları sıfırla
        if hasattr(self, 'bars_drawn'):
            delattr(self, 'bars_drawn')
        if hasattr(self, 'labels_drawn'):
            delattr(self, 'labels_drawn')
        self.draw_array()
        self.info_label.configure(text=f"Yeni liste oluşturuldu - {self.array_size} eleman")
    
    def draw_array(self, highlighted_indices=None, swapped_indices=None):
        if not self.array:
            return
        
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            return
        
        # İlk kez çiziliyorsa tüm canvas'ı temizle
        if not hasattr(self, 'bars_drawn'):
            self.canvas.delete("all")
            self.bars_drawn = {}
            self.labels_drawn = {}
        
        bar_width = canvas_width / len(self.array)
        max_value = max(self.array) if self.array else 1
        
        for i, value in enumerate(self.array):
            x1 = i * bar_width
            x2 = (i + 1) * bar_width - 2
            y1 = canvas_height
            y2 = canvas_height - (value / max_value) * (canvas_height - 20)
            
            # Renk belirleme
            if highlighted_indices and i in highlighted_indices:
                color = "#ff6b6b"  # Kırmızı - karşılaştırılan
            elif swapped_indices and i in swapped_indices:
                color = "#4ecdc4"  # Turkuaz - yer değiştirilen
            else:
                color = "#74b9ff"  # Mavi - normal
            
            # Eğer bu çubuk zaten çizilmişse, rengini ve pozisyonunu güncelle
            if i in self.bars_drawn:
                self.canvas.itemconfig(self.bars_drawn[i], fill=color)
                # Çubuk pozisyonunu güncelle
                self.canvas.coords(self.bars_drawn[i], x1, y1, x2, y2)
                # Değer etiketi güncelle (küçük listeler için)
                if len(self.array) <= 50 and i in self.labels_drawn:
                    self.canvas.itemconfig(self.labels_drawn[i], text=str(value))
                    # Etiket pozisyonunu da güncelle
                    self.canvas.coords(self.labels_drawn[i], (x1 + x2) / 2, y2 - 10)
            else:
                # Yeni çubuk çiz
                bar_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                self.bars_drawn[i] = bar_id
                
                # Değer etiketi (küçük listeler için)
                if len(self.array) <= 50:
                    label_id = self.canvas.create_text(
                        (x1 + x2) / 2, y2 - 10,
                        text=str(value),
                        fill="white",
                        font=("Arial", 8)
                    )
                    self.labels_drawn[i] = label_id
        
        self.root.update()
    
    def start_sorting(self):
        if self.is_sorting:
            return
        
        self.is_sorting = True
        self.sort_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.generate_btn.configure(state="disabled")
        
        # Sıralama işlemini ayrı thread'de başlat
        thread = threading.Thread(target=self.run_sorting)
        thread.daemon = True
        thread.start()
    
    def stop_sorting(self):
        self.is_sorting = False
        self.sort_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.generate_btn.configure(state="normal")
        self.info_label.configure(text="Sıralama durduruldu")
    
    def run_sorting(self):
        try:
            algorithm = self.algorithms[self.current_algorithm]
            self.info_label.configure(text=f"{self.current_algorithm} çalışıyor...")
            
            # Algoritma çalıştır
            algorithm()
            
            if self.is_sorting:
                self.info_label.configure(text=f"{self.current_algorithm} tamamlandı!")
                self.sort_btn.configure(state="normal")
                self.stop_btn.configure(state="disabled")
                self.generate_btn.configure(state="normal")
                self.is_sorting = False
                
        except Exception as e:
            self.info_label.configure(text=f"Hata: {str(e)}")
            self.stop_sorting()
    
    def update_display(self, highlighted_indices=None, swapped_indices=None):
        if not self.is_sorting:
            return
        
        self.draw_array(highlighted_indices, swapped_indices)
        time.sleep(self.sorting_speed)
    
    # Sıralama algoritmaları
    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if not self.is_sorting:
                    return
                
                # Karşılaştırma
                self.update_display(highlighted_indices=[j, j + 1])
                
                if self.array[j] > self.array[j + 1]:
                    # Yer değiştirme
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.update_display(swapped_indices=[j, j + 1])
    
    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            if not self.is_sorting:
                return
            
            min_idx = i
            for j in range(i + 1, n):
                if not self.is_sorting:
                    return
                
                self.update_display(highlighted_indices=[i, j])
                
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            
            if min_idx != i:
                self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
                self.update_display(swapped_indices=[i, min_idx])
    
    def insertion_sort(self):
        for i in range(1, len(self.array)):
            if not self.is_sorting:
                return
            
            key = self.array[i]
            j = i - 1
            
            while j >= 0 and self.array[j] > key:
                if not self.is_sorting:
                    return
                
                self.update_display(highlighted_indices=[j, j + 1])
                self.array[j + 1] = self.array[j]
                j -= 1
            
            self.array[j + 1] = key
            self.update_display(swapped_indices=[j + 1])
    
    def quick_sort(self):
        def _quick_sort(arr, low, high):
            if not self.is_sorting:
                return
            
            if low < high:
                pi = self._partition(arr, low, high)
                _quick_sort(arr, low, pi - 1)
                _quick_sort(arr, pi + 1, high)
        
        _quick_sort(self.array, 0, len(self.array) - 1)
    
    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if not self.is_sorting:
                return low
            
            self.update_display(highlighted_indices=[j, high])
            
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.update_display(swapped_indices=[i, j])
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.update_display(swapped_indices=[i + 1, high])
        return i + 1
    
    def merge_sort(self):
        def _merge_sort(arr, left, right):
            if not self.is_sorting:
                return
            
            if left < right:
                mid = (left + right) // 2
                _merge_sort(arr, left, mid)
                _merge_sort(arr, mid + 1, right)
                self._merge(arr, left, mid, right)
        
        _merge_sort(self.array, 0, len(self.array) - 1)
    
    def _merge(self, arr, left, mid, right):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            if not self.is_sorting:
                return
            
            self.update_display(highlighted_indices=[k])
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            if not self.is_sorting:
                return
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            if not self.is_sorting:
                return
            arr[k] = right_arr[j]
            j += 1
            k += 1
        
        self.update_display()
    
    def heap_sort(self):
        def heapify(arr, n, i):
            if not self.is_sorting:
                return
            
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                self.update_display(highlighted_indices=[i, largest])
                arr[i], arr[largest] = arr[largest], arr[i]
                self.update_display(swapped_indices=[i, largest])
                heapify(arr, n, largest)
        
        n = len(self.array)
        
        # Max heap oluştur
        for i in range(n // 2 - 1, -1, -1):
            heapify(self.array, n, i)
        
        # Heap'ten elemanları çıkar
        for i in range(n - 1, 0, -1):
            if not self.is_sorting:
                return
            
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.update_display(swapped_indices=[0, i])
            heapify(self.array, i, 0)
    
    def shell_sort(self):
        n = len(self.array)
        gap = n // 2
        
        while gap > 0:
            for i in range(gap, n):
                if not self.is_sorting:
                    return
                
                temp = self.array[i]
                j = i
                
                while j >= gap and self.array[j - gap] > temp:
                    if not self.is_sorting:
                        return
                    
                    self.update_display(highlighted_indices=[j, j - gap])
                    self.array[j] = self.array[j - gap]
                    j -= gap
                
                self.array[j] = temp
                self.update_display(swapped_indices=[j])
            
            gap //= 2
    
    def radix_sort(self):
        def counting_sort(exp):
            n = len(self.array)
            output = [0] * n
            count = [0] * 10
            
            for i in range(n):
                if not self.is_sorting:
                    return
                index = (self.array[i] // exp) % 10
                count[index] += 1
            
            for i in range(1, 10):
                count[i] += count[i - 1]
            
            for i in range(n - 1, -1, -1):
                if not self.is_sorting:
                    return
                index = (self.array[i] // exp) % 10
                output[count[index] - 1] = self.array[i]
                count[index] -= 1
            
            for i in range(n):
                if not self.is_sorting:
                    return
                self.array[i] = output[i]
                self.update_display(highlighted_indices=[i])
        
        max_val = max(self.array)
        exp = 1
        
        while max_val // exp > 0:
            if not self.is_sorting:
                return
            counting_sort(exp)
            exp *= 10
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SortingVisualizer()
    app.run()
