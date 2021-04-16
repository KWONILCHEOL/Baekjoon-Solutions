using System;
using System.IO;
using System.Windows.Forms;
using Microsoft.WindowsAPICodePack.Dialogs;
namespace makeJson
{
    public partial class Baekjoon : Form
    {
        public Baekjoon()
        {
            InitializeComponent();
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            CommonOpenFileDialog ofd = new CommonOpenFileDialog();
            ofd.IsFolderPicker = true;
            if (ofd.ShowDialog() != CommonFileDialogResult.Ok)
                return;
            textBox1.Text = ofd.FileName;
            string[] dirs = Directory.GetDirectories(textBox1.Text);
            int size = dirs.Length;
            string[] id = new string[size];
            string[] level = new string[size];
            string[] title = new string[size];
            string[] category = new string[size];
            string[] link = new string[size];
            string[] language = new string[size];
            string data = "";
            for (int i = 0; i < size; i++)
            {
                string filename = Path.GetFileName(dirs[i]);
                id[i] = filename.Split(' ')[0].Substring(4);
                level[i] = filename.Substring(1, 2);
                title[i] = filename.Substring(id[i].Length + level[i].Length + 3);
                category[i] = "연습문제";

                string temp = filename.Replace("[",@"%5B").Replace("]",@"%5D").Replace(" ",@"%20");
                link[i] = string.Format("[문제](https://www.acmicpc.net/problem/{0}) / [풀이](/solutions/{1}/)",id[i], temp);
                string[] files = Directory.GetFiles(dirs[i]);
                foreach(string file in files)
                {
                    string ext = Path.GetExtension(file).Substring(1);
                    if(ext == "py")
                        language[i] += string.Format("[![python3](/assets/python3.svg)](/solutions/{1}/submit.{0}) ", ext, temp);
                    else
                        language[i] += string.Format("[![{0}](/assets/{0}.svg)](/solutions/{1}/submit.{0}) ", ext, temp);
                }
                data += string.Format("| {0} | {1} | {2} | {3} | {4} | {5} |\n", id[i], level[i], title[i], category[i], link[i], language[i]);
            }
            File.WriteAllText(textBox1.Text + "\\data.txt", data);
        }
    }
}
