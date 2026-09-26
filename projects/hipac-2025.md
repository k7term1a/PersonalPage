# 2025 第四屆國網盃應用程式效能優化競賽（HiPAC 2025）季軍 / HiPAC 2025, 3rd Place

- 時間：2025
- 主辦：國家高速網路與計算中心（NCHC）
- 隊名：Attention（國立臺中教育大學），6 人
- 名次：季軍；冠亞軍皆為清華大學
- 來源：決賽簡報（HiPAC2025_NTCU_Attention）、NCHC 成果頁、我的筆記 https://hackmd.io/@kaichi/Sy9UKzCUex

## 我的分工
- **Slurm 建置與效能監控**：計算節點裝 DCGM + DCGM-Exporter（9400），監控節點從原始碼編譯 Prometheus（9090）並架 Grafana（3000）；
  透過 `/etc/slurm/prolog` 與 Slurm job 整合；踩過的坑：DCGM 要走官方套件教學，用 GitHub repo 方式會找不到 `libdcgm.so.4`
- **LAMMPS 調參**與撰寫 job 繳交腳本（Python 自動產生 sbatch 與 input 檔送 Slurm 掃參數）
- **隱藏題 SU2（流體力學）**：現場讀文件完成 meson 建置（MPI / MKL / CUDA），約 20 分鐘跑通，但調參結果不如其他隊伍
- LLM 服務化題不是我負責

## 環境
每節點 8×V100、2 CPU、4 Infiniband、2 Ethernet，共兩節點。
軟體堆疊：MLNX_OFED、自建 UCX、NVIDIA driver / CUDA、自建 MPI。

## 賽題與做法
1. **系統建置與監控**：拓樸探索與 binding script；DCGM exporter + Node exporter + Prometheus + Grafana + Slurm
2. **HPL**：以 objdump 靜態分析驗證二進位對 V100（sm70）相容性，取代逐一試跑；
   Slurm / cgroup / numactl 處理 CPU binding；調 N、NB、cores-per-rank
   - 台灣杉二號練習：N=245760、NB=256 達 9.005e4 GFlops
   - 比賽機三次繳交：4.943e4 → 5.8e4 → 6.324e4 GFlops（理論上限約 118.9 TFlops）
3. **Qiskit**：Lab1 量子電路（XOR 約束）；Lab2 模擬器加速：從原始碼建置（CUDA + MPI + MKL，比 pip 快 5～10%）、
   改用 CUDA-Q、雙精度改單精度、多 GPU；執行時間 65s → 21s → 8s
4. **LAMMPS**：GPU 版（sm_70、double）建置；Python 腳本自動產生 sbatch 與 input 檔送 Slurm 掃參數
5. **隱藏題 1 SU2（流體力學）**：meson 建置啟用 MPI / MKL / CUDA，約 20 分鐘完成
6. **隱藏題 2**：LLM 部署與服務化（vLLM）

## 技能對應
Slurm、Prometheus、Grafana、DCGM、HPL 調校、CUDA / CUDA-Q、Qiskit、LAMMPS、vLLM 部署

