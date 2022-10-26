# FinalReport 期末專題的專案空間

使用教學參考文章:
單人操作: http://tech-marsw.logdown.com/blog/2013/08/16/git-notes-github
多人合作: http://tech-marsw.logdown.com/blog/2013/08/17/git-notes-github-n-person-cooperation-settings

分支名稱說明:
master(主分支): "維持最終版本狀態"，不允許任何中途 merge，只有當 develop 完成測試後，才會 merge 到這做展示。
develop(開發中分支): "存放階段性版本"，允許各方開發版本到此進行 merge，並且在此解決版本衝突，完成階段性任務，確定運行順利後，才會 merge 到 master。
小組隊員們的分支 * 6: "雲端功能"，提供一個雲端儲存地點，確保每次作業完都能上傳，不會造成資料遺失或臨時想開啟卻放在本地端的窘境。
